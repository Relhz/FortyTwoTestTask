# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Requests.date_and_time'
        db.delete_column(u'hello_requests', 'date_and_time')

        # Adding field 'Requests.requests_date_time'
        db.add_column(u'hello_requests', 'requests_date_time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Info.jabber'
        db.alter_column(u'hello_info', 'jabber', self.gf('django.db.models.fields.EmailField')(max_length=50, null=True))

        # Changing field 'Info.email'
        db.alter_column(u'hello_info', 'email', self.gf('django.db.models.fields.EmailField')(max_length=50, null=True))

    def backwards(self, orm):
        # Adding field 'Requests.date_and_time'
        db.add_column(u'hello_requests', 'date_and_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 6, 8, 0, 0)),
                      keep_default=False)

        # Deleting field 'Requests.requests_date_time'
        db.delete_column(u'hello_requests', 'requests_date_time')


        # Changing field 'Info.jabber'
        db.alter_column(u'hello_info', 'jabber', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Info.email'
        db.alter_column(u'hello_info', 'email', self.gf('django.db.models.fields.EmailField')(max_length=254, null=True))

    models = {
        u'hello.info': {
            'Meta': {'object_name': 'Info'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u'Surname'", 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'hello.requests': {
            'Meta': {'object_name': 'Requests'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "u'Post'", 'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'default': "u'path'", 'max_length': '300'}),
            'requests_date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']