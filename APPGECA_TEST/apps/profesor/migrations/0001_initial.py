# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-07 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumno', '0001_initial'),
        ('instrumento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alumno', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='alumno.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=200)),
                ('fecha', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('evaluado', models.BooleanField(default=False)),
                ('asignados', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profesor.Asignados')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('cedula_profesor', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='Cedula')),
                ('nombre_profesor', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellido_profesor', models.CharField(max_length=40, verbose_name='Apellido')),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instrumento.Instrumento')),
            ],
        ),
        migrations.AddField(
            model_name='evaluado',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profesor.Profesor'),
        ),
        migrations.AddField(
            model_name='asignados',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profesor.Profesor'),
        ),
    ]
