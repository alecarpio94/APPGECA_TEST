#!/usr/bin/python   
# -*- coding: utf-8 -*-
from django import forms
from ...apps.profesor.models import *
from ...apps.utils.forms_date import DateInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import itertools

#########################FORMULARIO PROFESOR######################
class ProfForm(UserCreationForm):
	css_error_class = 'has-error'

	class Meta:
		model = Profesor

		fields = ['cedula_profesor', 'nombre_profesor', 'apellido_profesor','asignacion']

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kargs)
			for filed in self.fields:
				self.fields[filed].widgets.attrs.update({'class':'form-control'})
