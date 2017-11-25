from __future__ import unicode_literals

from django.db import models

# Create your models here.
######################MODELO INSTRUMENTO###################
class Instrumento(models.Model):

	inst = (('Programa Alma Llanera','Programa Alma Llanera'),
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

	nombr_instr = models.CharField('Nombre',primary_key=True,choices=inst, max_length=50, unique=True)
	stock_min = models.IntegerField('Cantidad Minima',default=1)
	stock_max = models.IntegerField('Cantidad Maxima',default=0)
	disponibles = models.IntegerField('Disponibles',default=0)
	uso = models.IntegerField('Uso',default=0)

	def save(self, *args, **kwargs):
		if (self.stock_max) > (self.stock_min):
			super(Instrumento, self).save(*args, **kwargs)
			if (self.disponibles+1)< (self.stock_max):
				super(Instrumento, self).save(*args, **kwargs)
			else:
				self.disponibles = 0
				super(Instrumento, self).save(*args, **kwargs)

	def __unicode__(self):
		Dato = "%s"% (self.nombr_instr)
		return Dato
