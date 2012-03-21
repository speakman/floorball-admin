# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Participant'
        db.create_table('attendance_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('nin', self.gf('django.db.models.fields.CharField')(max_length=11, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('attendance', ['Participant'])

        # Adding model 'Gathering'
        db.create_table('attendance_gathering', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('attendance', ['Gathering'])

        # Adding M2M table for field participants on 'Gathering'
        db.create_table('attendance_gathering_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gathering', models.ForeignKey(orm['attendance.gathering'], null=False)),
            ('participant', models.ForeignKey(orm['attendance.participant'], null=False))
        ))
        db.create_unique('attendance_gathering_participants', ['gathering_id', 'participant_id'])


    def backwards(self, orm):
        
        # Deleting model 'Participant'
        db.delete_table('attendance_participant')

        # Deleting model 'Gathering'
        db.delete_table('attendance_gathering')

        # Removing M2M table for field participants on 'Gathering'
        db.delete_table('attendance_gathering_participants')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nin': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['attendance']
