# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-22 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0017_auto_20181122_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='voluntarios',
        ),
        migrations.AddField(
            model_name='evento',
            name='departamentos',
            field=models.ManyToManyField(to='ong.Voluntario', verbose_name='Departamentos'),
        ),
    ]
