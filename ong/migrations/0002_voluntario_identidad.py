# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voluntario',
            name='identidad',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
