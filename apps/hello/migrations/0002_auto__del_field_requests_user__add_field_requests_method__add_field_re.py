# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Requests.user'
        db.delete_column(u'hello_requests', 'user')

        # Adding field 'Requests.method'
        db.add_column(u'hello_requests', 'method',
                      self.gf('django.db.models.fields.CharField')(default=u'Post', max_length=10),
                      keep_default=False)

        # Adding field 'Requests.status_code'
        db.add_column(u'hello_requests', 'status_code',
                      self.gf('django.db.models.fields.CharField')(default=u'200', max_length=10),
                      keep_default=False)


        # Changing field 'Requests.date_and_time'
        db.alter_column(u'hello_requests', 'date_and_time', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Adding field 'Requests.user'
        db.add_column(u'hello_requests', 'user',
                      self.gf('django.db.models.fields.CharField')(default=u'Anonimous user', max_length=30),
                      keep_default=False)

        # Deleting field 'Requests.method'
        db.delete_column(u'hello_requests', 'method')

        # Deleting field 'Requests.status_code'
        db.delete_column(u'hello_requests', 'status_code')


        # Changing field 'Requests.date_and_time'
        db.alter_column(u'hello_requests', 'date_and_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

    models = {
        u'hello.info': {
            'Meta': {'object_name': 'Info'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_of_birst': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u'Surname'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'hello.requests': {
            'Meta': {'object_name': 'Requests'},
            'date_and_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 5, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "u'Post'", 'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'default': "u'path'", 'max_length': '300'}),
        }
    }

    complete_apps = ['hello']
