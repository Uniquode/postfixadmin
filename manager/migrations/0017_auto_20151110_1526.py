# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_auto_20151105_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapValue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('is_active', models.BooleanField(verbose_name='Active', default=True)),
                ('key', models.CharField(max_length=255)),
                ('v1', models.TextField(blank=True, verbose_name='Value 1')),
                ('v2', models.TextField(blank=True, verbose_name='Value 2', null=True)),
                ('v3', models.TextField(blank=True, verbose_name='Value 3', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='mapvalues',
            name='map',
        ),
        migrations.AlterField(
            model_name='map',
            name='fn1',
            field=models.CharField(max_length=64, verbose_name='Fieldname 1', default='Value'),
        ),
        migrations.AlterField(
            model_name='map',
            name='fn2',
            field=models.CharField(blank=True, max_length=64, verbose_name='Fieldname 2', null=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='fn3',
            field=models.CharField(blank=True, max_length=64, verbose_name='Fieldname 3', null=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Map Name', unique=True),
        ),
        migrations.DeleteModel(
            name='MapValues',
        ),
        migrations.AddField(
            model_name='mapvalue',
            name='map',
            field=models.ForeignKey(to='manager.Map'),
        ),
    ]
