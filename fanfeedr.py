# Create your views here.
import urllib
import re
import simplejson
from django.conf import settings
from gameday.models import University, League

def sync_schools(team=settings.FANFEEDR_TEAM):
    """
    From the default school listed in FANFEEDR_TEAM
    grabs the latest games and checks to see if there is a school
    in the database for the opposite team. If not, it will insert the
    school and make all the league links for the school.
    """
    
    url = settings.FANFEEDR_SCORES_URL
    
    values = {
        'appid':    settings.FANFEEDR_API,
        'format':   'json',
        'resource': team,
        'start':    '0',
        'rows':     '25',
    }
    
    data = urllib.urlencode(values)
    result = simplejson.load(urllib.urlopen(url, data))
        
    teams = {}
    
    for game in result['docs']:
        winteam = re.search(r'(?P<league>[^/]+)/(?P<school>[^/]+)$', game['winteamlink'])
        loseteam = re.search(r'(?P<league>[^/]+)/(?P<school>[^/]+)$', game['loseteamlink'])
            
        if not teams.has_key(winteam.groupdict()['school']):
           teams[winteam.groupdict()['school']] = {
                'school': game['winteamname'], 
                'league': winteam.groupdict()['league']
            }
        if not teams.has_key(loseteam.groupdict()['school']):
            teams[loseteam.groupdict()['school']] = {
                'school': game['loseteamname'], 
                'league': loseteam.groupdict()['league']
            }
    
    for key, meta in teams.iteritems():
        league, school = ''
        try:
            league = League.objects.get(league=meta['league'])
        except League.DoesNotExist:
            league = League(league=meta['league']).save()
        try:
            school = University.objects.get(school_key=key)
            school.leagues.add(league)
        except University.DoesNotExist:
            school = University(name=meta['school'], school_key=key)
            school.save()
            school.leagues.add(league)

    return teams
