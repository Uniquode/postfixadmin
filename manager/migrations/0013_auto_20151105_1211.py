# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20151105_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='f1',
            new_name='fn1',
        ),
        migrations.RenameField(
            model_name='map',
            old_name='f2',
            new_name='fn2',
        ),
        migrations.RenameField(
            model_name='map',
            old_name='f3',
            new_name='fn3',
        ),
    ]
