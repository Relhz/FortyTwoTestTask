# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("hello", "0009_auto__add_modelsaction__add_info__chg_field_requests_requests_date_tim"),
    )

    def forwards(self, orm):

        # Deleting field 'ModelsAction.action_date_time'
        db.delete_column(u'hello_modelsaction', 'action_date_time')

        # Adding field 'ModelsAction.creation'
        db.add_column(u'hello_modelsaction', 'creation',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Adding field 'ModelsAction.action_date_time'
        db.add_column(u'hello_modelsaction', 'action_date_time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ModelsAction.creation'
        db.delete_column(u'hello_modelsaction', 'creation')


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
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "u'photos/no-avatar.jpg'", 'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'hello.modelsaction': {
            'Meta': {'object_name': 'ModelsAction'},
            'action': ('django.db.models.fields.CharField', [], {'default': "u'edit'", 'max_length': '20'}),
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelname': ('django.db.models.fields.CharField', [], {'default': "u'info'", 'max_length': '30'})
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