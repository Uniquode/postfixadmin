# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_auto_20151110_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='disposition',
            field=models.CharField(max_length=255, verbose_name='Default Disposition', blank=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='fn1',
            field=models.CharField(max_length=64, verbose_name='Field Name 1', default='Value'),
        ),
        migrations.AlterField(
            model_name='map',
            name='fn2',
            field=models.CharField(max_length=64, null=True, blank=True, verbose_name='Field Name 2'),
        ),
        migrations.AlterField(
            model_name='map',
            name='fn3',
            field=models.CharField(max_length=64, null=True, blank=True, verbose_name='Field Name 3'),
        ),
    ]
