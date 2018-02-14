# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 01:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_auto_20180203_2224'),
        ('feed', '0003_feed_entry_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed_entry',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='groups.Group'),
            preserve_default=False,
        ),
    ]