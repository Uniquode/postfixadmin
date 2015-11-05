# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_domain_allow_mailbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='auth_source',
            field=models.TextField(verbose_name='Authentication Source', blank=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='allow_mailbox',
            field=models.BooleanField(verbose_name='Allow New Mailboxes', default=True),
        ),
    ]
