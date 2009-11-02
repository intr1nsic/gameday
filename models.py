from django.db import models
import datetime
from django.contrib.localflavor.us.models  import USStateField

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=200)
    school_key = models.CharField(max_length=200, blank=True, null=True, editable=False, unique=True)
    school_link = models.CharField(max_length=200, blank=True, null=True)
    leagues = models.ManyToManyField('League', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True,
        help_text='What city is the University in?')
    state = USStateField(blank=True, null=True)
    zip = models.IntegerField(max_length=5, blank=True, null=True)
    fieldhouse = models.CharField(max_length=200, blank=True, null=True,
        help_text='What is the name of the Fieldhouse?')
    stadium = models.CharField(max_length=200, blank=True, null=True,
        help_text='What is the name of the stadium?')
    track = models.CharField(max_length=200, blank=True, null=True,
        help_text='What is the name of the track and field?')
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
        
class League(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    league = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.league
        
class Schedule(models.Model):
        
    game_time = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    winteam = models.ForeignKey(University, related_name='winning_school', blank=True, null=True)
    loseteam = models.ForeignKey(University, related_name='loosing_school', blank=True, null=True)
    winscore = models.IntegerField(blank=True, null=True)
    losescore = models.IntegerField(blank=True, null=True)
    league = models.ForeignKey(League)
    status = models.CharField(max_length=100, blank=True, null=True)
    eventlink = models.CharField(max_length=200, unique=True)
    update_game = models.BooleanField(help_text='Should we automatically update information for this game?', default=True)
    
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
    
    def __unicode__(self):
        return self.name
    