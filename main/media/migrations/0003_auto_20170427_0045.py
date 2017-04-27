# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20170408_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]