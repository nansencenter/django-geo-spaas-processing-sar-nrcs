# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-29 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_auto_20160705_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('catalog.dataset',),
        ),
    ]