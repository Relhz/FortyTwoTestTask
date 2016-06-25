# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Requests'
        pass


    def backwards(self, orm):

        # Deleting model 'Requests'
        pass


    models = {
        u'hello.requests': {
            'Meta': {'object_name': 'Requests'},
            'requests_date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 6, 7, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "u'Post'", 'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'default': "u'path'", 'max_length': '300'})
        }
    }

    complete_apps = ['hello']