# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('igcloned', '0008_auto_20181006_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='profile',
        ),
    ]
