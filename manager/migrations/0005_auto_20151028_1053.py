# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20151028_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailbox',
            name='disposition',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Full Name'),
        ),
    ]
