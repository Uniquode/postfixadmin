# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_vacation'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vacation',
            unique_together=set([('mailbox',)]),
        ),
    ]
