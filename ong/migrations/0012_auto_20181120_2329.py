# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-21 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0011_auto_20181102_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voluntario',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos_voluntarios'),
        ),
    ]