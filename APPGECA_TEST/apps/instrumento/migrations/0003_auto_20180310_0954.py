# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-10 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumento', '0002_auto_20180310_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='asignatura',
            name='instrumento',
        ),
        migrations.DeleteModel(
            name='Asignatura',
        ),
    ]