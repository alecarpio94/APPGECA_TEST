#!/usr/bin/python   
# -*- coding: utf-8 -*-
from django import forms
from ...apps.instrumento.models import *
from ...apps.utils.forms_date import DateInput
import itertools

########################FORMULARIO INSTRUMENTO####################
class InstrForm(forms.ModelForm):
	css_error_class = 'has-error'
	class Meta:
		model = Instrumento

		fields = ['nombr_instr' , 'stock_min' , 'stock_max', 'uso',]