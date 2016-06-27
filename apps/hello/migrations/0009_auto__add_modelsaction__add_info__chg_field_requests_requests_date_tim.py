# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("hello", "0008_auto_add_requests"),
    )

    def forwards(self, orm):
        # Adding model 'ModelsAction'
        db.create_table(u'hello_modelsaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modelname', self.gf('django.db.models.fields.CharField')(default=u'info', max_length=30)),
            ('action', self.gf('django.db.models.fields.CharField')(default=u'edit', max_length=20)),
            ('action_date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['ModelsAction'])


    def backwards(self, orm):
        # Deleting model 'ModelsAction'
        db.delete_table(u'hello_modelsaction')


    models = {
        u'hello.modelsaction': {
            'Meta': {'object_name': 'ModelsAction'},
            'action': ('django.db.models.fields.CharField', [], {'default': "u'edit'", 'max_length': '20'}),
            'action_date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelname': ('django.db.models.fields.CharField', [], {'default': "u'info'", 'max_length': '30'})
        },
    }

    complete_apps = ['hello']