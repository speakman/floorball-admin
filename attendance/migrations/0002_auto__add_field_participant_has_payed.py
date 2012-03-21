# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Participant.has_payed'
        db.add_column('attendance_participant', 'has_payed', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Participant.has_payed'
        db.delete_column('attendance_participant', 'has_payed')


    models = {
        'attendance.gathering': {
            'Meta': {'object_name': 'Gathering'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['attendance.Participant']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'attendance.participant': {
            'Meta': {'object_name': 'Participant'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'has_payed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nin': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['attendance']
