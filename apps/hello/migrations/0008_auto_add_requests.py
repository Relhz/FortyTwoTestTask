# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("hello", "0006_auto__add_field_info_photo"),
    )

    def forwards(self, orm):

        # Adding model 'Requests'
        db.create_table(u'hello_requests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(default=u'path', max_length=300)),
            ('method', self.gf('django.db.models.fields.CharField')(default=u'Post', max_length=10)),
            ('requests_date_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 6, 7, 0, 0)))
        ))
        db.send_create_signal(u'hello', ['Requests'])


    def backwards(self, orm):

        # Deleting model 'Requests'
        db.delete_table(u'hello_requests')


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