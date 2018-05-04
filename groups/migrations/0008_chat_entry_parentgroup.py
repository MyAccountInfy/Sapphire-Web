# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_chat_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_entry',
            name='parentGroup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='groups.Group'),
            preserve_default=False,
        ),
    ]