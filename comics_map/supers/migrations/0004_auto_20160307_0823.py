# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0003_super_first_appearance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='description',
        ),
        migrations.RemoveField(
            model_name='super',
            name='first_appearance',
        ),
        migrations.RemoveField(
            model_name='super',
            name='origin_state',
        ),
    ]
