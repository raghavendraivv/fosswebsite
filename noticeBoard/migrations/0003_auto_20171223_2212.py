# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-23 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeBoard', '0002_auto_20170924_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
