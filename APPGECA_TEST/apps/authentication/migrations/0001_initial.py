# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-12 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumno', '0001_initial'),
        ('profesor', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ci', models.CharField(blank=True, max_length=8, unique=True, verbose_name='C\xe9dula')),
                ('username', models.CharField(blank=True, default='ci', max_length=40, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=40, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=100)),
                ('is_secretaria', models.BooleanField(default=False, verbose_name='Secretaria')),
                ('is_profesor', models.BooleanField(default=False, verbose_name='Profesor')),
                ('is_alumno', models.BooleanField(default=False, verbose_name='Alumno')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff Status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser Status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Sate Joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ci_alumno', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alumno.Alumno')),
                ('ci_profesor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profesor.Profesor')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
