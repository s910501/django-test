# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170510_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPlace',
            fields=[
            ],
            options={
                'proxy': True,
                'ordering': ['address'],
            },
            bases=('news.place',),
        ),
    ]