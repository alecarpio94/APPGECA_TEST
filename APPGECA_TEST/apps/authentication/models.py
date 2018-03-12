#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.translation import ugettext, ugettext_lazy as apodo
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.conf import settings
from ...apps.utils.selects import Selects

# Create your models here.

class UsersManager(BaseUserManager):
    def create_user(self, ci, password=None, **kwargs):
        if not ci:
            raise ValueError('Users must have a valid ci.')

        account = self.model(
            ci=self.model.normalize_username(ci)
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, ci, password, **kwargs):
        account = self.create_user(ci, password, **kwargs)

        account.is_superuser = True
        account.is_staff = True
        account.save()
        return account

class Users(AbstractBaseUser, PermissionsMixin):
    
    ci = models.CharField(_('Cédula'),max_length=8, null=False, unique=True, blank=True)
    ci_profesor = models.OneToOneField(settings.AUTH_PROFESOR_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    ci_alumno = models.OneToOneField(settings.AUTH_ALUMNO_MODEL, null=True, blank=True)
    username = models.CharField(_('username'), max_length=40, blank=True ,default="ci")
    first_name = models.CharField(_('first name'), max_length=40, blank=True)
    last_name = models.CharField(_('last name'), max_length=40, blank=True)
    email = models.EmailField(_('Email'), blank=True)
    password = models.CharField(max_length=100, null=False)

    is_secretaria = models.BooleanField(_('Secretaria'), default=False)
    is_profesor = models.BooleanField(_('Profesor'), default=False)
    is_alumno= models.BooleanField(_('Alumno'), default=False)

    is_active= models.BooleanField(_('Active'), default=True)
    is_staff=models.BooleanField(_('Staff Status'), default=False)
    is_superuser=models.BooleanField(_('Superuser Status'), default=False)

    date_joined = models.DateTimeField(_('Sate Joined'), default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsersManager()

    USERNAME_FIELD = 'ci'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return '%s %s %s %s'%(self.ci,self.ci_profesor, self.first_name, self.last_name)

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name]).encode('utf-8').strip()

    def get_short_name(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if self.username:
            self.username = self.ci
            super(Users, self).save(*args, **kwargs)

