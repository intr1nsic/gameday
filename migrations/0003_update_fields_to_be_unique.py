
from south.db import db
from django.db import models
from gameday.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Game.eventlink'
        db.add_column('gameday_game', 'eventlink', orm['gameday.game:eventlink'])
        
        # Creating unique_together for [school_key] on University.
        db.create_unique('gameday_university', ['school_key'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [school_key] on University.
        db.delete_unique('gameday_university', ['school_key'])
        
        # Deleting field 'Game.eventlink'
        db.delete_column('gameday_game', 'eventlink')
        
    
    
    models = {
        'gameday.game': {
            'League': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameday.League']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'eventlink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losescore': ('django.db.models.fields.IntegerField', [], {}),
            'loseteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loosing_school'", 'to': "orm['gameday.University']"}),
            'winscore': ('django.db.models.fields.IntegerField', [], {}),
            'winteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'winning_school'", 'to': "orm['gameday.University']"})
        },
        'gameday.league': {
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
