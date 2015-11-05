# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_auto_20151105_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapvalues',
            name='value',
        ),
        migrations.AddField(
            model_name='maps',
            name='f1',
            field=models.CharField(max_length=64, verbose_name='Field#1 Name', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maps',
            name='f2',
            field=models.CharField(blank=True, null=True, verbose_name='Field#2 Name', max_length=64),
        ),
        migrations.AddField(
            model_name='maps',
            name='f3',
            field=models.CharField(blank=True, null=True, verbose_name='Field#3 Name', max_length=64),
        ),
        migrations.AddField(
            model_name='mapvalues',
            name='v1',
            field=models.TextField(blank=True, verbose_name='Value#1'),
        ),
        migrations.AddField(
            model_name='mapvalues',
            name='v2',
            field=models.TextField(blank=True, null=True, verbose_name='Value#2'),
        ),
        migrations.AddField(
            model_name='mapvalues',
            name='v3',
            field=models.TextField(blank=True, null=True, verbose_name='Value#3'),
        ),
    ]
