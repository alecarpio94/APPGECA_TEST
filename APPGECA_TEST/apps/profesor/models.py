from __future__ import unicode_literals

from django.db import models
from ...apps.utils.selects import Selects

# Create your models here.
####################MODELO PROFESOR########################
class Profesor(models.Model):

	asig = (('Programa Alma Llanera','Programa Alma Llanera'),
		('Arpa Clasica','Arpa Clasica'),
		('Orquesta Infantil','Orquesta Infantil'),
		('Oboe','Oboe'),
		('Cuatro','Cuatro'),
		('Percusion','Percusion'),
		('Violincello','Violincello'),
		('Trombon','Trombon'),
		('Coro/Lenguaje Musical','Coro/Lenguaje Musical'),
		('Flauta/Lenguaje Musical','Flauta/Lenguaje Musical'),
		('Corno','Corno'),
		('Guitarra','Guitarra'),
		('Violin','Violin'),
		('Viola','Viola'),
		('Viola/Lenguaje Musical','Viola/Lenguaje Musical'),
		('Flauta','Flauta'),
		('Clarinete','Clarinete'),
		('Tuba','Tuba'),
		('Trompeta/Lenguaje Musical','Trompeta/Lenguaje Musical'),
		('Contrabajo','Contrabajo'),
		('Pianista','Pianista'))

	cedula_profesor = models.IntegerField('Cedula',primary_key=True, unique=True)
	nombre_profesor = models.CharField('Nombre',max_length=100)
	apellido_profesor = models.CharField('Apellido',max_length=100)
	asignacion = models.CharField('Asignacion',max_length=40, choices=asig, default=0)
	
	def __unicode__(self):
		Dato = "%i"% (self.cedula_profesor)
		return Dato
