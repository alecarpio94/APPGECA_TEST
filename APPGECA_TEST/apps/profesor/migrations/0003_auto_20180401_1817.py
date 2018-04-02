# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-01 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0002_auto_20180313_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=11)),
                ('cargo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalObrero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=11)),
                ('cargo', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='profesor',
            name='telefono',
            field=models.CharField(default=1, max_length=11, verbose_name='Telefono'),
            preserve_default=False,
        ),
    ]
