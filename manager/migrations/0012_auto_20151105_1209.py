# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_auto_20151105_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('is_active', models.BooleanField(verbose_name='Active', default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('f1', models.CharField(max_length=64, verbose_name='Field#1 Name', default='Value')),
                ('f2', models.CharField(max_length=64, verbose_name='Field#2 Name', null=True, blank=True)),
                ('f3', models.CharField(max_length=64, verbose_name='Field#3 Name', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='mapvalues',
            name='map',
            field=models.ForeignKey(to='manager.Map'),
        ),
        migrations.DeleteModel(
            name='Maps',
        ),
    ]
