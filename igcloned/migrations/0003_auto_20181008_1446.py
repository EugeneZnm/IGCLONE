# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 11:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('igcloned', '0002_auto_20181008_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='profile',
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='igcloned.Image'),
        ),
    ]
