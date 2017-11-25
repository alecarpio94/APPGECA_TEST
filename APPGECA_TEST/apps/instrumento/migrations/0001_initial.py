# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-25 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombr_instr', models.CharField(choices=[('Programa Alma Llanera', 'Programa Alma Llanera'), ('Arpa Clasica', 'Arpa Clasica'), ('Orquesta Infantil', 'Orquesta Infantil'), ('Oboe', 'Oboe'), ('Cuatro', 'Cuatro'), ('Percusion', 'Percusion'), ('Violincello', 'Violincello'), ('Trombon', 'Trombon'), ('Coro/Lenguaje Musical', 'Coro/Lenguaje Musical'), ('Flauta/Lenguaje Musical', 'Flauta/Lenguaje Musical'), ('Corno', 'Corno'), ('Guitarra', 'Guitarra'), ('Violin', 'Violin'), ('Viola', 'Viola'), ('Viola/Lenguaje Musical', 'Viola/Lenguaje Musical'), ('Flauta', 'Flauta'), ('Clarinete', 'Clarinete'), ('Tuba', 'Tuba'), ('Trompeta/Lenguaje Musical', 'Trompeta/Lenguaje Musical'), ('Contrabajo', 'Contrabajo'), ('Pianista', 'Pianista')], max_length=50, unique=True)),
                ('stock_min', models.IntegerField(default=0)),
                ('stock_max', models.IntegerField(default=0)),
                ('disponibles', models.IntegerField(default=0)),
                ('uso', models.IntegerField(default=0)),
            ],
        ),
    ]
