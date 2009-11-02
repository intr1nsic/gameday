
from south.db import db
from django.db import models
from gameday.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Schedule.name'
        # (to signature: django.db.models.fields.CharField(max_length=200, null=True, blank=True))
        db.alter_column('gameday_schedule', 'name', orm['gameday.schedule:name'])
        
        # Changing field 'Schedule.game_time'
        # (to signature: django.db.models.fields.DateTimeField(default=datetime.datetime.now))
        db.alter_column('gameday_schedule', 'game_time', orm['gameday.schedule:game_time'])
        
        # Changing field 'Schedule.loseteam'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['gameday.University']))
        db.alter_column('gameday_schedule', 'loseteam_id', orm['gameday.schedule:loseteam'])
        
        # Changing field 'Schedule.winteam'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['gameday.University']))
        db.alter_column('gameday_schedule', 'winteam_id', orm['gameday.schedule:winteam'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Schedule.name'
        # (to signature: django.db.models.fields.CharField(max_length=200))
        db.alter_column('gameday_schedule', 'name', orm['gameday.schedule:name'])
        
        # Changing field 'Schedule.game_time'
        # (to signature: django.db.models.fields.DateTimeField())
        db.alter_column('gameday_schedule', 'game_time', orm['gameday.schedule:game_time'])
        
        # Changing field 'Schedule.loseteam'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['gameday.University']))
        db.alter_column('gameday_schedule', 'loseteam_id', orm['gameday.schedule:loseteam'])
        
        # Changing field 'Schedule.winteam'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['gameday.University']))
        db.alter_column('gameday_schedule', 'winteam_id', orm['gameday.schedule:winteam'])
        
    
    
    models = {
        'gameday.league': {
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'gameday.schedule': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'eventlink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'game_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameday.League']"}),
            'losescore': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'loseteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loosing_school'", 'blank': 'True', 'null': 'True', 'to': "orm['gameday.University']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'winscore': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'winteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'winning_school'", 'blank': 'True', 'null': 'True', 'to': "orm['gameday.University']"})
        },
        'gameday.university': {
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fieldhouse': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leagues': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['gameday.League']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'school_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'null': 'True', 'blank': 'True'}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['gameday']
