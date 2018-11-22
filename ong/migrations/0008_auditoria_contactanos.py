# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 05:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ong', '0007_auto_20181025_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.TextField()),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contactanos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=9)),
                ('correo', models.EmailField(blank=True, max_length=100)),
                ('mensaje', models.TextField()),
                ('fecha_hora', models.DateTimeField()),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
    ]