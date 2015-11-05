# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_auto_20151105_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailbox',
            name='credential',
            field=models.TextField(blank=True, verbose_name='Password'),
        ),
    ]
