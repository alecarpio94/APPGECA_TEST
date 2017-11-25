from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Actividad(models.Model):

	codigo_act = models.IntegerField(default=0, primary_key=True)
	nombr_acti = models.CharField(max_length=150)
	descripcio = models.TextField(max_length=500)
	fecha_inic = models.DateField(auto_now=False)
	fecha_fina = models.DateField(auto_now=False)

	def __unicode__(self):
		Dato = "%s"% (self.nombr_acti)
		return Dato
