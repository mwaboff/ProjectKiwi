# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_auto_20170912_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='orig_url',
            field=models.URLField(verbose_name='original URL'),
        ),
    ]
