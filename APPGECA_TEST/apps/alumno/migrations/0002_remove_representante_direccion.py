# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-13 03:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representante',
            name='direccion',
        ),
    ]
