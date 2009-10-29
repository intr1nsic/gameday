# Create your views here.
import urllib
import re
import simplejson
from django.conf import settings
from gameday.models import University, League

def get_university():
    """
    Grabs the last played teams from the default school
    """
    
    url = settings.FANFEEDR_SCORES_URL
    
    values = {
        'appid':    settings.FANFEEDR_API,
        'format':   'json',
        'resource': settings.FANFEEDR_TEAM,
        'start':    '0',
        'rows':     '25',
    }
    
    data = urllib.urlencode(values)
    result = simplejson.load(urllib.urlopen(url, data))
    
    current_schools = University.objects.all()
    
    teams = {}
    
    for game in result['docs']:
        winteam = re.search(r'([^/]+)$', game['winteamlink']).group(1)
        loseteam = re.search(r'([^/]+)$', game['winteamlink']).group(1)        

        if not teams.has_key(winteam):
           teams[winteam] = game['winteamname']
        if not teams.has_key(loseteam):
            teams[loseteam] = game['loseteamname']
    
    for key, name in teams.iteritems():
        try:
            University.objects.get(school_key=key)
        except University.DoesNotExist:
            University(name=name, school_key=key).save()
    
    return teams
