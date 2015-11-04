# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20151028_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alias',
            old_name='goto',
            new_name='disposition',
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='disposition',
            field=models.TextField(null=True, blank=True),
        ),
    ]
