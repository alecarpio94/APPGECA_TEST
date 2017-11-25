#!/usr/bin/python   
# -*- coding: utf-8 -*-
from django import forms
from ...apps.actividad.models import *
from ...apps.utils.forms_date import DateInput
import itertools

###################FORMULARIO ACTIVIDAD###########################
class ActivForm(forms.ModelForm):

	class Meta:
		model = Actividad

		fields = ['codigo_act', 'nombr_acti', 'descripcio', 'fecha_inic', 'fecha_fina']
		labels = {
		'codigo_act': 'Codigo De La Actividad',
		'nombr_acti': 'Nombre De La Actividad',
		'descripcio': 'Descripcion',
		'fecha_inic': 'Fecha De Inicio',
		'fecha_fina': 'Fecha De Culminacion',
		}
		widgets = {
        'fecha_inic': DateInput(format='%Y-%m-%d'),
        'fecha_fina': DateInput(format='%Y-%m-%d'),
        }

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for fields in self.fields:
			self.fields[filed].widgets.attrs.update({'class':'form-control'})
