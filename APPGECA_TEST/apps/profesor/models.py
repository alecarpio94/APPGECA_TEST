#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as apodo
from django.utils import timezone
from django.db import models
from django.conf import settings
from ...apps.utils.selects import Selects
from ...apps.alumno.models import Alumno
from ...apps.instrumento.models import Instrumento

# Create your models here.
####################MODELO PROFESOR########################
class Profesor(models.Model):

	cedula_profesor = models.CharField(apodo('Cedula'),max_length=8,primary_key=True, null=False, unique=True)
	nombre_profesor = models.CharField(apodo('Nombre'),max_length=40)
	apellido_profesor = models.CharField(apodo('Apellido'),max_length=40)
	asignacion = models.ForeignKey(Instrumento)

	def __unicode__(self):
		return '%s'%(self.cedula_profesor)

	def get_full_name(self):
		return '%s %s'%(self.nombre_profesor, self.apellido_profesor)

class Asignados(models.Model):
	
	id = models.AutoField(primary_key=True)
	profesor = models.ForeignKey(Profesor,null=True)
	alumno = models.OneToOneField(Alumno,null=True)

	def __unicode__(self):
		return '{}'.format(self.alumno)

	def get_full_name(self):
		return '%s %s'%(self.alumno, self.profesor)

class Evaluado(models.Model):

	id = models.AutoField(primary_key=True)
	profesor = models.ForeignKey(Profesor,null=True)
	asignados = models.ForeignKey(Asignados,null=True)
	descripcion = models.TextField(max_length=200)
	fecha = models.DateField(auto_now=False)
	status = models.BooleanField(default=False, blank=True)
	evaluado = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return '%s %s'%(self.profesor, self.asignados)

	def get_full_name(self):
		return '{}'.format(self.asignados)
	