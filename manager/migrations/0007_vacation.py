# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20151028_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('is_active', models.BooleanField(verbose_name='Active', default=True)),
                ('response_subject', models.CharField(max_length=255)),
                ('response_body', models.TextField()),
                ('cache', models.TextField(editable=False)),
                ('mailbox', models.OneToOneField(to='manager.Mailbox')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
