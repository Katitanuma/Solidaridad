# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-21 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0013_auto_20181120_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='depto',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
