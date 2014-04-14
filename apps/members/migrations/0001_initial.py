# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'members_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'members', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'members_member')


    models = {
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['members']