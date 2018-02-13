# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-04 03:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0005_auto_20180124_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='events',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slots',
        ),
        migrations.RemoveField(
            model_name='group',
            name='organizers',
        ),
        migrations.AddField(
            model_name='group',
            name='organizers',
            field=models.ManyToManyField(related_name='group_organizers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='group',
            name='volunteers',
        ),
        migrations.AddField(
            model_name='group',
            name='volunteers',
            field=models.ManyToManyField(related_name='group_volunteers', to=settings.AUTH_USER_MODEL),
        ),
    ]
