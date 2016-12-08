# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=255)),
                ('disposition', models.TextField()),
            ],
            options={
                'db_table': 'alias',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('transport', models.CharField(max_length=255, blank=True)),
                ('disposition', models.CharField(max_length=255, verbose_name='Default Disposition', blank=True)),
                ('maxquota_mb', models.IntegerField(default=0, verbose_name='Max Quota')),
                ('is_backup_mx', models.BooleanField(default=False, verbose_name='Backup MX')),
                ('allow_mailbox', models.BooleanField(default=True, verbose_name='Allow New Mailboxes')),
                ('auth_source', models.TextField(verbose_name='Authentication Source', blank=True)),
            ],
            options={
                'db_table': 'domain',
            },
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('username', models.CharField(max_length=255)),
                ('credential', models.TextField(verbose_name='Password', blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('quota_mb', models.IntegerField(default=0, verbose_name='Quota')),
                ('disposition', models.TextField(null=True, blank=True)),
                ('vacation_enabled', models.BooleanField(default=False)),
                ('vacation_subject', models.CharField(max_length=255, null=True, blank=True)),
                ('vacation_body', models.TextField(null=True, blank=True)),
                ('vacation_cache', models.TextField(null=True, blank=True, editable=False)),
                ('domain', models.ForeignKey(null=True, to='manager.Domain')),
            ],
            options={
                'db_table': 'mailbox',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=64, verbose_name='Map Name', unique=True)),
                ('fn1', models.CharField(default='Value', max_length=64, verbose_name='Field Name 1')),
                ('fn2', models.CharField(max_length=64, verbose_name='Field Name 2', null=True, blank=True)),
                ('fn3', models.CharField(max_length=64, verbose_name='Field Name 3', null=True, blank=True)),
            ],
            options={
                'db_table': 'map',
            },
        ),
        migrations.CreateModel(
            name='MapValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('key', models.CharField(max_length=255)),
                ('v1', models.TextField(verbose_name='Value 1', blank=True)),
                ('v2', models.TextField(verbose_name='Value 2', null=True, blank=True)),
                ('v3', models.TextField(verbose_name='Value 3', null=True, blank=True)),
                ('map', models.ForeignKey(to='manager.Map')),
            ],
            options={
                'db_table': 'mapvalue',
            },
        ),
        migrations.AlterUniqueTogether(
            name='map',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='alias',
            name='domain',
            field=models.ForeignKey(null=True, to='manager.Domain'),
        ),
        migrations.AlterUniqueTogether(
            name='mapvalue',
            unique_together=set([('map', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='mailbox',
            unique_together=set([('domain', 'username')]),
        ),
        migrations.AlterUniqueTogether(
            name='alias',
            unique_together=set([('domain', 'name')]),
        ),
    ]
