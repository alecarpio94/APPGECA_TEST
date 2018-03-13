from __future__ import unicode_literals
from django.utils.translation import ugettext, ugettext_lazy as apodo
from django.db import models
from django.utils import timezone
from datetime import datetime, date, timedelta
# Create your models here.
class Actividad(models.Model):

	id = models.AutoField(primary_key=True)
	nombr_acti = models.CharField(apodo("Nombre De La Actividad"),max_length=150,)
	descripcio = models.TextField(apodo("Descripcion"),max_length=500)
	fecha_inic = models.DateField(apodo("Fecha De Inicio"), blank=True, null=True)
	hora_inico = models.TimeField(apodo("Hora De Inicio"))
	hora_final = models.TimeField(apodo("Hora De Culminacion"))
	fecha_fina = models.DateField(apodo("Fecha De Culminacion"), blank=True, null=True)
	status1 = models.BooleanField(default=False)
	status2 = models.BooleanField(default=False)
	status3 = models.BooleanField(default=False)

	def __unicode__(self):
		return '%s'%(self.nombr_acti)

	def save(self, *args, **kwargs):
		fecha = self.fecha_inic
		fecha_dada = self.fecha_fina
		horaI = self.hora_inico
		horaF = self.hora_final
		if fecha_dada >= fecha:
			if horaF >= horaI:
				print ("Si Paso")
				super(Actividad, self).save(*args, **kwargs)
			else:
				print ("No Paso")

	def fecha(self):		
		 return datetime.strptime(str(self.fecha_inic.date()), "%Y-%m-%d").strftime("%Y-%m-%d")

	def hora(self):
		return "12:50"