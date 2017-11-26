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
from ...apps.utils.mixins import AdminRequiredMixin, ProfesorRequiredMixin
from ...apps.utils.forms_date import DateInput
from django.utils.decorators import method_decorator
import os

######################PROFESOR ADMIN####################
class profCreateView(LoginRequiredMixin,AdminRequiredMixin, CreateView):
	model = Profesor
	fields = ['cedula_profesor', 'nombre_profesor', 'apellido_profesor', 'asignacion']
	template_name = 'profesor/crear-profesor.html'
	success_url = '/listado_de_profesor/'

class profListView(LoginRequiredMixin,AdminRequiredMixin,ProfesorRequiredMixin,ListView):
	context_object_name = 'Listaprofesor'
	model = Profesor
	template_name = 'profesor/list-profesor.html'

class profMListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listaprofesor'
	model = Profesor
	template_name = 'profesor/mostr-profesor.html'

class profUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
	template_name = 'profesor/editar-profesor.html'
	model = Profesor
	fields = ['cedula_profesor', 'nombre_profesor', 'apellido_profesor', 'asignacion']
	success_url = '/listado_de_profesor/'

class profDeleteView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):

	model = Profesor
	template_name = 'profesor/profesor_confirm_delete.html'
	success_url = reverse_lazy('profesor:list_profesor')

class profListAllView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	def get_context_data(self, **kwargs):
	    context = super(profListAllView, self).get_context_data(**kwargs)
	    context['date'] = datetime.now().strftime("%d/%m/%Y")
	    return context

	context_object_name = 'ListaAllprofesor'
	model = Profesor
	template_name = 'reportes/report-prof-list.html'
