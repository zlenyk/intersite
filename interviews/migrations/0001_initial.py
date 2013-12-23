# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'interviews_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'interviews', ['Comment'])

        # Adding model 'Interview'
        db.create_table(u'interviews_interview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'interviews', ['Interview'])

        # Adding M2M table for field comments on 'Interview'
        m2m_table_name = db.shorten_name(u'interviews_interview_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('interview', models.ForeignKey(orm[u'interviews.interview'], null=False)),
            ('comment', models.ForeignKey(orm[u'interviews.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['interview_id', 'comment_id'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'interviews_comment')

        # Deleting model 'Interview'
        db.delete_table(u'interviews_interview')

        # Removing M2M table for field comments on 'Interview'
        db.delete_table(db.shorten_name(u'interviews_interview_comments'))


    models = {
        u'interviews.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'interviews.interview': {
            'Meta': {'object_name': 'Interview'},
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['interviews.Comment']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'people.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['interviews']