# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-24 10:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170424_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 24, 10, 33, 42, 726968, tzinfo=utc)),
        ),
    ]
