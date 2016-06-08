# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Requests'
        db.delete_table(u'hello_requests')

        # Deleting field 'Info.photo'
        db.delete_column(u'hello_info', 'photo')

        # Deleting field 'Info.date_of_birth'
        db.delete_column(u'hello_info', 'date_of_birth')


    def backwards(self, orm):
        # Adding model 'Requests'
        db.create_table(u'hello_requests', (
            ('status_code', self.gf('django.db.models.fields.CharField')(default=u'200', max_length=10)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_and_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 6, 5, 0, 0))),
            ('path', self.gf('django.db.models.fields.CharField')(default=u'path', max_length=300)),
            ('method', self.gf('django.db.models.fields.CharField')(default=u'Post', max_length=10)),
        ))
        db.send_create_signal(u'hello', ['Requests'])

        # Adding field 'Info.photo'
        db.add_column(u'hello_info', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Info.date_of_birth'
        db.add_column(u'hello_info', 'date_of_birth',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'hello.info': {
            'Meta': {'object_name': 'Info'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u'Surname'", 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']