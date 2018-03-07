from __future__ import unicode_literals
from django.utils import timezone
import datetime
from django.db import models
from APPGECA_TEST.apps.alumno.models import Alumno

# Create your models here.
######################MODELO INSTRUMENTO###################
class Instrumento(models.Model):

	id = models.AutoField(primary_key=True)
	nombr_instr = models.CharField('Nombre', max_length=50, unique=True)

	def __str__(self):
		return '{}'.format(self.nombr_instr)

class Asignatura(models.Model):

	id = models.AutoField(primary_key=True, unique=True)
	instrumento = models.ForeignKey(Instrumento)
	alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
	descripcion = models.TextField()
	fecha_entrega = models.CharField(max_length=10)
	fecha_retiro = models.CharField(max_length=10,blank=True, null=True)

	def __str__(self):
		return '{} {}'.format(self.alumno, self.instrumento)

	def instrumentos(self):
		return '{} {}'.format(self.instrumento)