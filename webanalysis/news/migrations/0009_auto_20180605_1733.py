# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-05 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20180605_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(default=True, verbose_name='首页显示'),
        ),
        migrations.AlterField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(default=True, verbose_name='导航显示'),
        ),
    ]
