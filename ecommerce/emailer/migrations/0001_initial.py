# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import tagulous.models.models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='_Tagulous_EmailGroup_email_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='EmailAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_name', models.CharField(help_text=b'', max_length=100, verbose_name=b'Action name')),
            ],
            options={
                'verbose_name': 'Email Action',
                'verbose_name_plural': 'Email Actions',
            },
        ),
        migrations.CreateModel(
            name='EmailFrom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_from_name', models.CharField(help_text=b'', max_length=500, verbose_name=b'Email From')),
                ('email_id', models.CharField(help_text=b'', max_length=100, verbose_name=b'Email Id', blank=True)),
            ],
            options={
                'verbose_name': 'Email From',
                'verbose_name_plural': 'Email From Data',
            },
        ),
        migrations.CreateModel(
            name='EmailGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(help_text=b'', max_length=1000, verbose_name=b'Group name')),
                ('description', ckeditor.fields.RichTextField(help_text=b'Enter a text which will be shown on top of the image', max_length=5000, verbose_name=b'Group description', blank=True)),
                ('group_type', models.IntegerField(choices=[(1, b'Customer Care'), (2, b'Managers')])),
                ('email_list', tagulous.models.fields.TagField(space_delimiter=True, case_sensitive=False, to='emailer._Tagulous_EmailGroup_email_list', help_text=b'Enter comma seperated email ids', _set_tag_meta=True, verbose_name=b'Email list')),
            ],
            options={
                'verbose_name': 'Email Group',
                'verbose_name_plural': 'Email Groups',
            },
        ),
        migrations.CreateModel(
            name='EmailSave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_from', models.CharField(help_text=b'', max_length=255, null=True, verbose_name=b'Email From', blank=True)),
                ('email_to', models.TextField(help_text=b'', verbose_name=b'Email To', blank=True)),
                ('email_subject', models.TextField(help_text=b'', null=True, verbose_name=b'Email Subject', blank=True)),
                ('email_body', models.TextField(help_text=b'', null=True, verbose_name=b'Email Body', blank=True)),
                ('email_sent_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Email Sent On', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.CharField(help_text=b'', max_length=1000, verbose_name=b'Template name')),
                ('email_subject', models.CharField(help_text=b'', max_length=500, verbose_name=b'Email subject', blank=True)),
                ('email_body', ckeditor.fields.RichTextField(help_text=b'', max_length=5000, verbose_name=b'Email body', blank=True)),
            ],
            options={
                'verbose_name': 'Email Template',
                'verbose_name_plural': 'Email Templates',
            },
        ),
        migrations.AddField(
            model_name='emailaction',
            name='email_from',
            field=models.ForeignKey(related_name='email_action_for_email_from', blank=True, to='emailer.EmailFrom', null=True),
        ),
        migrations.AddField(
            model_name='emailaction',
            name='email_group',
            field=models.ForeignKey(related_name='email_action_for_group', blank=True, to='emailer.EmailGroup', null=True),
        ),
        migrations.AddField(
            model_name='emailaction',
            name='email_template',
            field=models.ForeignKey(related_name='email_action_for_template', blank=True, to='emailer.EmailTemplate', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='_tagulous_emailgroup_email_list',
            unique_together=set([('slug',)]),
        ),
    ]
