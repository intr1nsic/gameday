
from south.db import db
from django.db import models
from gameday.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'University'
        db.create_table('gameday_university', (
            ('id', orm['gameday.University:id']),
            ('name', orm['gameday.University:name']),
            ('school_key', orm['gameday.University:school_key']),
            ('school_link', orm['gameday.University:school_link']),
            ('city', orm['gameday.University:city']),
            ('state', orm['gameday.University:state']),
            ('zip', orm['gameday.University:zip']),
            ('fieldhouse', orm['gameday.University:fieldhouse']),
            ('stadium', orm['gameday.University:stadium']),
            ('track', orm['gameday.University:track']),
        ))
        db.send_create_signal('gameday', ['University'])
        
        # Adding model 'League'
        db.create_table('gameday_league', (
            ('id', orm['gameday.League:id']),
            ('name', orm['gameday.League:name']),
            ('league', orm['gameday.League:league']),
            ('description', orm['gameday.League:description']),
        ))
        db.send_create_signal('gameday', ['League'])
        
        # Adding ManyToManyField 'University.leagues'
        db.create_table('gameday_university_leagues', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('university', models.ForeignKey(orm.University, null=False)),
            ('league', models.ForeignKey(orm.League, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'University'
        db.delete_table('gameday_university')
        
        # Deleting model 'League'
        db.delete_table('gameday_league')
        
        # Dropping ManyToManyField 'University.leagues'
        db.delete_table('gameday_university_leagues')
        
    
    
    models = {
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
            'school_key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'school_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'null': 'True', 'blank': 'True'}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['gameday']
