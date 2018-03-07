#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
from django.views.generic import View
#________________________________________
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseForbidden, HttpResponseRedirect
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
from django.views.generic import ListView 
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
#paginacion de django#
from ...apps.profesor.models import *
from ...apps.profesor.forms import *
from ...apps.authentication.models import Users
from ...apps.authentication.forms import UsersModelForm
from ...apps.utils.mixins import AdminRequiredMixin, ProfesorRequiredMixin
from ...apps.utils.forms_date import DateInput
from django.utils.decorators import method_decorator
import os

######################PROFESOR ADMIN####################
class ProfCreateView(LoginRequiredMixin,AdminRequiredMixin, CreateView):
	model = Profesor
	fields = ['cedula_profesor', 'nombre_profesor', 'apellido_profesor','asignacion']
	template_name = 'profesor/crear_profesor.html'
	success_url = reverse_lazy('profesor:list_profesor')

######################LISTADO DE LOS PROFESORES######################
class ProfListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listaprofesor'
	model = Profesor
	template_name = 'profesor/lista_de_profesores.html'

######################LISTA DE ALUMNOS ASIGANDOS AL PROFESOR######################
class ProfAlumListView(LoginRequiredMixin,ListView):
	context_object_name = 'Listaalumnos'
	model = Asignados
	template_name = 'profesor/listado_alumno_profesor.html'

	def get_context_data(self, **kwargs):
	    context = super(ProfAlumListView, self).get_context_data(**kwargs)
	    user_login = self.request.user
	    if user_login:
	    	profesor_login = user_login.ci_profesor
	    	if profesor_login:
	    		alumnos_profesor = Asignados.objects.filter(profesor = profesor_login)
	    		if alumnos_profesor:
	    			context['object_list'] = alumnos_profesor
	    		else:
	    			context['object_list'] = None
	    	else:
	    		context['object_list'] = None
	    else:
	    	context['object_list'] = None
	    return context

class AsigAlumListView(LoginRequiredMixin,ListView):
	context_object_name = 'Listaalumnos'
	model = Asignados
	template_name = 'asignacion/listado_alumnos_asignados.html'

######################PONDERACION DEL ALUMNOS PROFESOR######################
class EvaAlumListView(LoginRequiredMixin,ProfesorRequiredMixin,CreateView):
	model = Evaluado
	fields = ['asignados','descripcion', 'fecha' ,'status' , 'evaluado']
	template_name = 'profesor/evaluacion_del_alumno.html'
	success_url = reverse_lazy('profesor:list_alumn')

	def get_context_data(self, **kwargs):
	    context = super(EvaAlumListView, self).get_context_data(**kwargs)
	    user_login = self.request.user
	    if user_login:
	    	profesor_login = user_login.ci_profesor
	    	if profesor_login:
	    		alumnos_profesor = Evaluado.objects.filter(profesor = profesor_login)
	    		if alumnos_profesor:
	    			context['Evaluado'] = alumnos_profesor
	    		else:
	    			context['Evaluado'] = None
	    	else:
	    		context['Evaluado'] = None
	    else:
	    	context['Evaluado'] = None
	    return context

######################ACTUALIZAR PROFESOR######################
class ProfUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
	template_name = 'profesor/editar_profesor.html'
	model = Profesor
	fields = ['cedula_profesor', 'nombre_profesor', 'apellido_profesor', 'asignacion']
	success_url = reverse_lazy('profesor:list_profesor')

######################ELIMINAR PROFESOR######################
class ProfDeleteView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):
	model = Profesor
	template_name = 'profesor/profesor_confirm_delete.html'
	success_url = reverse_lazy('profesor:list_profesor')

######################REPORTE DE LA LISTA DE LOS PROFESORES######################
class ProfListAllView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	def get_context_data(self, **kwargs):
	    context = super(ProfListAllView, self).get_context_data(**kwargs)
	    context['date'] = datetime.now().strftime("%d/%m/%Y")
	    return context

	context_object_name = 'ListaAllprofesor'
	model = Profesor
	template_name = 'reportes/report-prof-list.html'

#######################ASIGNAR ALUMNO AL PROFESOR################################
class AlumAsigView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
	model = Asignados
	fields = ['profesor','alumno']
	template_name = 'asignacion/asignacion_profesor_alumno.html'
	success_url = reverse_lazy('profesor:alumno_profesor')

#######################RETIRAR ALUMNO DEL PROFESOR#######################
class RetiroAlumnoView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):
	template_name = 'asignacion/asignados_confirm_delete.html'
	model = Asignados
	success_url = reverse_lazy('profesor:alumno_profesor')