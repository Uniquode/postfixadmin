# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_auto_20151105_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='allow_mailbox',
            field=models.BooleanField(verbose_name='Allow Mailboxes', default=True),
        ),
    ]
