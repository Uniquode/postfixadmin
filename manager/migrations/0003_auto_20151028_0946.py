# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('username', models.CharField(max_length=255)),
                ('credential', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('quota_mb', models.IntegerField(default=0, verbose_name='Quota')),
                ('maildir', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='admin',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='alias',
            name='domain',
            field=models.ForeignKey(to='manager.Domain', null=True),
        ),
        migrations.AddField(
            model_name='alias',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='created',
            field=models.DateTimeField(verbose_name='Created on', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='alias',
            name='created',
            field=models.DateTimeField(verbose_name='Created on', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='alias',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='created',
            field=models.DateTimeField(verbose_name='Created on', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='alias',
            unique_together=set([('domain', 'address')]),
        ),
        migrations.AddField(
            model_name='mailbox',
            name='domain',
            field=models.ForeignKey(to='manager.Domain', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='mailbox',
            unique_together=set([('domain', 'username')]),
        ),
    ]
