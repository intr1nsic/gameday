# Create your views here.
import urllib
import re
import sys
import simplejson
from django.conf import settings
from dateutil import parser
from gameday.models import University, League, Schedule

def _get_results(resource, url):
    """
    Take the url and resource and query fanfeedr
    return the json value string
    """
            
    values = {
        'appid':    settings.FANFEEDR_API,
        'format':   'json',
        'resource': resource,
        'start':    '0',
        'rows':     '25',
    }
    
    data = urllib.urlencode(values)
    try:
        results = simplejson.load(urllib.urlopen(url, data))
    except IOError:
        return 'There was an error connecting to the feed'
    return results

def sync_schools(resource=settings.FANFEEDR_TEAM, url=settings.FANFEEDR_SCHEDULE_URL, *args, **kwargs):
    """
    From the default school listed in FANFEEDR_TEAM
    grabs the latest games and checks to see if there is a school
    in the database for the opposite team. If not, it will insert the
    school and make all the league links for the school.
    """
   
    results = _get_results(resource, url)
    
    
    
    for game in results:
        
        # Grab our home and away team from the schedule ( keys )
        awayteam = re.search(r'(?P<league>[^/]+)/(?P<school>[^/]+)$', game['away']['team'])
        hometeam = re.search(r'(?P<league>[^/]+)/(?P<school>[^/]+)$', game['home']['team'])
        
        league, no_league = League.objects.get_or_create(league=awayteam.groupdict()['league'])
        awayteam, make_awayteam = University.objects.get_or_create(school_key=awayteam.groupdict()['school'])
        hometeam, make_hometeam = University.objects.get_or_create(school_key=hometeam.groupdict()['school'])
        
        # Ugly, but lets got a display name for the teams instead of the keys
        [display_away, display_home] = game['name'].split(' @ ')
        
        # Finish creating our new schools with a Display Name
        if make_awayteam or make_hometeam:
            if make_awayteam:
                awayteam.name = display_away
                awayteam.save()
            if make_hometeam:
                hometeam.name = display_home
                hometeam.save()
        
        # Lets add the respected leagues now
        try:
            awayteam.leagues.add(league)
        except:
            pass
        try:
            hometeam.leagues.add(league)
        except:
            pass

def sync_schedule(resource=settings.FANFEEDR_TEAM, url=settings.FANFEEDR_SCHEDULE_URL, *args, **kwargs):
    
    results = _get_results(resource, url)
    
    for game in results:
        
        # Combine our date and time to get game time
        game_time = parser.parse(game['date'] + ' ' + game['time'])
        
        # Grab our away and home team with their respected league
        awayteam = re.search(r'(?P<league>[^/]+)/(?P<school>[^/]+)$', game['away']['team'])
        hometeam = re.search(r'(?P<league>[^/]+)/(?P<school>[^/]+)$', game['home']['team'])
        
        # Get our leauge
        league = League.objects.get(league=awayteam.groupdict()['league'])
        
        try:
            awayteam = University.objects.get(school_key=awayteam.groupdict()['school'])
            hometeam = University.objects.get(school_key=hometeam.groupdict()['school'])
        except ObjectDoesNotExist:
            sys.exit("There was a problem resolving the teams")
        
        # Find out our winning and losing score
        if game['away']['score'] > game['home']['score']:
            [winscore, winteam] = game['away']['score'], awayteam
            [losescore, loseteam] = game['home']['score'], hometeam
        else:
            [winscore, winteam] = game['home']['score'], hometeam
            [losescore, loseteam] = game['away']['score'], awayteam        
            
        schedule, make_schedule = Schedule.objects.get_or_create(league=league, eventlink=game['resource_text'])
        
        # Because they may edit the schedule details, we will only add this on the initial insert
        # After its inserted, its fair game to be changed.
        if make_schedule or schedule.update_game:
            schedule.game_time = game_time
            schedule.name = game['name']
            schedule.winteam = winteam
            schedule.loseteam = loseteam
            schedule.winscore = winscore
            schedule.losescore = losescore
            if not game['status']:
                schedule.status = 'T.B.A.'
            else:
                schedule.status = game['status']
            schedule.save()            