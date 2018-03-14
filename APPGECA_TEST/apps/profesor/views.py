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
from django.views.generic import (
	CreateView,
	ListView,
	UpdateView,
	DeleteView,
	TemplateView, 
	FormView, 
	ListView, 
	TemplateView, 
	DetailView
	)
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

######################PONDERACION DEL ALUMNOS PROFESOR######################
class EvaAlumListView(LoginRequiredMixin,ProfesorRequiredMixin,CreateView):
	model = Evaluado
	fields = ['asignados','descripcion','fecha','status','evaluado']
	template_name = 'profesor/evaluacion_del_alumno.html'
	success_url = reverse_lazy('profesor:alumn_evalu')

	def form_valid(self, form):
		docente = get_object_or_404(Profesor, cedula_profesor=self.kwargs['pk'])
		evaluacion = form.save(commit=False)
		evaluacion.profesor =  docente
		evaluacion.save()
		return super(EvaAlumListView, self).form_valid(form)
		

	def get_context_data(self, *args,**kwargs):
	    context = super(EvaAlumListView, self).get_context_data(**kwargs)
	    user_login = self.request.user

	    if user_login:
	    	profesor_login = user_login.ci
	    	profesor = Profesor.cedula_profesor
	    	if profesor_login:
	    		if profesor:
		    		alumnos_profesor = Asignados.objects.get(profesor = profesor_login)
		    		if alumnos_profesor:
		    			print alumnos_profesor
		    			context['evaluado'] = alumnos_profesor
		    		else:
	    				context['evaluado'] = None
    			else:	
    				context['evaluado'] = None
	    	else:
	    		context['evaluado'] = None
	    else:
	    	context['evaluado'] = None
	    return context

#######################ASIGNAR ALUMNO AL PROFESOR################################
class AlumAsigView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
	model = Asignados
	fields = ['profesor','alumno']
	template_name = 'asignacion/asignacion_profesor_alumno.html'
	success_url = reverse_lazy('profesor:alumno_profesor')
	mensaje = ""

	def form_valid(self, form):
		if form.save(commit=False):
			return super(AlumAsigView, self).form_valid(form)
		else:
			mensaje = "El Alumno ya ha sido asignado a un profesor"
			return render(self.request, self.template_name, {'form':form, 'mensaje':self.mensaje})

######################LISTADO DE LOS PROFESORES######################
class ProfListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listaprofesor'
	model = Profesor
	template_name = 'profesor/lista_de_profesores.html'

######################LISTA DE ALUMNOS ASIGANDOS AL PROFESOR######################
class ProfAlumListView(LoginRequiredMixin,ListView):
	context_object_name = 'Lista'
	model = Asignados
	template_name = 'profesor/listado_alumno_profesor.html'

	def get_context_data(self, **kwargs):
	    context = super(ProfAlumListView, self).get_context_data(**kwargs)
	    user_login = self.request.user
	    profesor = Profesor
	    if user_login:
	    	profesor_login = user_login.ci
	    	profesor = Profesor.cedula_profesor
	    	if profesor_login:
	    		if profesor:
		    		alumnos_profesor = Asignados.objects.filter(profesor = profesor_login)
		    		if alumnos_profesor:
		    			context['object_list'] = alumnos_profesor
		    		else:
	    				context['object_list'] = None
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

class ListaAlumEvaluados(LoginRequiredMixin, ProfesorRequiredMixin, ListView):
	context_object_name = 'ListaEvalua'
	model = Evaluado
	template_name = 'profesor/lista_alumno_evaluado.html'

	def get_context_data(self, **kwargs):
	    context = super(ListaAlumEvaluados, self).get_context_data(**kwargs)
	    user_login = self.request.user
	    profesor = Profesor
	    if user_login:
	    	profesor_login = user_login.ci
	    	profesor = Profesor.cedula_profesor
	    	if profesor_login:
	    		if profesor:
		    		alumnos_profesor = Evaluado.objects.filter(profesor = profesor_login)
		    		if alumnos_profesor:
		    			context['object_list'] = alumnos_profesor
		    		else:
	    				context['object_list'] = None
    			else:	
    				context['object_list'] = None
	    	else:
	    		context['object_list'] = None
	    else:
	    	context['object_list'] = None
	    return context
		
##########################DETALLES DE LA EVALUACION###############################
class DetallesEvaluacionView(LoginRequiredMixin, ProfesorRequiredMixin, DetailView):
	context_object_name = 'Detalles'
	model = Evaluado
	template_name = 'profesor/detalles_evaluacion.html'
		
######################ACTUALIZAR EVALUACION######################
class UpdateEvaluacion(LoginRequiredMixin, ProfesorRequiredMixin, UpdateView):
	template_name = 'profesor/evaluacion_update.html'
	model = Evaluado
	fields = ['asignados','descripcion','fecha','status','evaluado']
	success_url = reverse_lazy('profesor:alumn_evalu')

######################ACTUALIZAR PROFESOR######################
class ProfUpdateView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
	template_name = 'profesor/editar_profesor.html'
	model = Profesor
	# fields = ['cedula_profesor', 'nombre_profesor', 'apellido_profesor', 'asignacion']
	success_url = reverse_lazy('profesor:list_profesor')

######################ELIMINAR PROFESOR######################
class ProfDeleteView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):
	model = Profesor
	template_name = 'profesor/profesor_confirm_delete.html'
	success_url = reverse_lazy('profesor:list_profesor')

#######################RETIRAR ALUMNO DEL PROFESOR#######################
class RetiroAlumnoView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):
	template_name = 'asignacion/asignados_confirm_delete.html'
	model = Asignados
	success_url = reverse_lazy('profesor:alumno_profesor')