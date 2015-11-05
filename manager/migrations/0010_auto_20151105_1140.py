# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20151028_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MapValues',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('key', models.CharField(max_length=255)),
                ('value', models.TextField()),
                ('map', models.ForeignKey(to='manager.Maps')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='vacation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='vacation',
            name='mailbox',
        ),
        migrations.AddField(
            model_name='mailbox',
            name='vacation_body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mailbox',
            name='vacation_cache',
            field=models.TextField(blank=True, null=True, editable=False),
        ),
        migrations.AddField(
            model_name='mailbox',
            name='vacation_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mailbox',
            name='vacation_subject',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Vacation',
        ),
    ]
