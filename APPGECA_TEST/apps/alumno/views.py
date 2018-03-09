#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
from django.views.generic import View
#________________________________________
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import Context
from django.template.context import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import date, datetime
from django.views.generic import CreateView 
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
#paginacion de django#
from ...apps.alumno.models import *
from ...apps.alumno.forms import *
from ...apps.authentication.models import Users
from ...apps.utils.mixins import AdminRequiredMixin,ProfesorRequiredMixin
from ...apps.utils.forms_date import DateInput
from django.utils.decorators import method_decorator
import os

#####################ALUMNO ADMIN#######################
class Prueba(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	model = Alumno
	form_class =  AlumForm
	second_form_class = RepreForm 
	three_form_class = VivienForm 
	four_form_class = DireccForm
	five_form_class = FamiliForm 
	six_form_class = EducaForm
	seven_form_class = EmpreForm
	eight_form_class = EducaMusiForm
	night_form_class = PercRepreForm
	ten_form_class = PercAlumForm
	template_name = 'alumno/crear_alumno.html'
	success_url = reverse_lazy('alumno:list_alumno')

	def get_context_data(self, **kwargs):
	    context = super(Prueba, self).get_context_data(**kwargs)
	    context['alumno'] = self.form_class
	    context['representante'] = self.second_form_class
	    context['vivienda'] = self.three_form_class
	    context['direccion'] = self.four_form_class
	    context['familia'] = self.five_form_class
	    context['educacion'] = self.six_form_class
	    context['empresa'] = self.seven_form_class
	    context['educamusi'] = self.eight_form_class
	    context['percrepre'] = self.night_form_class
	    context['percalum'] = self.ten_form_class
	    return context

	def post(self, request, *args, **kwargs):
		alumno = self.form_class(request.POST)
		representante = self.second_form_class(request.POST)
		vivienda = self.three_form_class(request.POST)
		direccion = self.four_form_class(request.POST)
		familia = self.five_form_class(request.POST)
		educacion = self.six_form_class(request.POST)
		empresa = self.seven_form_class(request.POST)
		educamusi = self.eight_form_class(request.POST)
		percrepre = self.night_form_class(request.POST)
		percalum = self.ten_form_class(request.POST)

		if alumno.is_valid() and representante.is_valid() and vivienda.is_valid() and direccion.is_valid() and familia.is_valid() and educacion.is_valid() and empresa.is_valid() and educamusi.is_valid() and percrepre.is_valid() and percalum.is_valid():
			f_alumno = alumno.save(commit=False)
			f_represetante = representante.save(commit=False)
			f_represetante.cedula_alumno = f_alumno
			f_vivienda = vivienda.save(commit=False)
			f_vivienda.cedula_alumno = f_alumno
			f_direccion = direccion.save(commit=False)
			f_direccion.cedula_alumno = f_alumno
			f_familia = familia.save(commit=False)
			f_familia.cedula_alumno = f_alumno
			f_educacion = educacion.save(commit=False)
			f_educacion.cedula_alumno = f_alumno
			f_empresa = empresa.save(commit=False)
			f_empresa.cedula_alumno = f_alumno
			f_educamusi = educamusi.save(commit=False)
			f_educamusi.cedula_alumno = f_alumno
			f_percrepre = percrepre.save(commit=False)
			f_percrepre.cedula_repres = f_represetante
			f_percalum = percalum.save(commit=False)
			f_percalum.cedula_alumno = f_alumno
			lista = [f_alumno, f_represetante, f_vivienda, f_direccion, f_familia, f_educacion, f_empresa, f_educamusi, f_percrepre, f_percalum]
			for i in lista:
				i.save()
			return HttpResponseRedirect(self.success_url)
		else:
			return render(request, self.template_name, {'alumno':alumno,
														'representante':representante,
														'vivienda':vivienda,
														'direccion':direccion,
														'familia':familia,
														'educacion':educacion,
														'empresa':empresa,
														'educamusi':educamusi,
														'percrepre':percrepre,
														'percalum':percalum, })

#######################LISTA GENERAL DE LOS ALUMNOS#######################
class AlumListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	model = Alumno
	template_name = 'alumno/lista_de_alumnos.html'
	context_object_name = 'alumno'

#######################ACTUALIZAR ALUMNO#######################
class AlumUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
	template_name = 'alumno/editar_alumno.html'
	model = Alumno
	fields = ['cedula_alumno','primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'sexo_alumno', 'fecha_nacimiento', 'lugar_nacimiento', 'nacionalidad', 'institucion']
	success_url = reverse_lazy('alumno:list_alumno')

#######################ELIMINAR ALUMNO#######################
class AlumDeleteView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):
	model = Alumno
	template_name = 'alumno/alumno_confirm_delete.html'
	success_url = reverse_lazy('alumno:list_alumno')

#######################INFORMACION GENERAL DEL ALUMNO#######################
class AlumnAllListView(LoginRequiredMixin, AdminRequiredMixin, DetailView):
	context_object_name = 'ListarAll'
	model = Alumno
	template_name = 'alumno/informacion_del_alumno.html'

