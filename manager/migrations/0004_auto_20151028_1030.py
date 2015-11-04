# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20151028_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailbox',
            old_name='maildir',
            new_name='disposition',
        ),
        migrations.AlterField(
            model_name='domain',
            name='is_backup_mx',
            field=models.BooleanField(verbose_name='Backup MX', default=False),
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='credential',
            field=models.TextField(verbose_name='Password'),
        ),
    ]
