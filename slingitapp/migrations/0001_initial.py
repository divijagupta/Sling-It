# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-17 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.URLField(max_length=100)),
                ('long_url', models.URLField(max_length=1000)),
                ('active_hits', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-active_hits'],
            },
        ),
    ]