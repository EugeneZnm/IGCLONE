# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igcloned', '0009_auto_20181006_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='igcloned.Likes'),
        ),
    ]