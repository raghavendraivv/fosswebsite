# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubManagement', '0002_auto_20170613_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='attendance',
            field=models.BooleanField(default=False),
        ),
    ]
