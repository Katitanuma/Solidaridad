# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0002_voluntario_identidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='BancoInformacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='archivos')),
            ],
        ),
    ]
