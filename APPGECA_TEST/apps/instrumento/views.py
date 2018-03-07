
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
from django.views.generic import CreateView, ListView,UpdateView,DeleteView
from django.views.generic import TemplateView, FormView, DetailView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
#paginacion de django#
from ...apps.instrumento.models import *
from ...apps.alumno.models import Alumno
from ...apps.instrumento.forms import *
from ...apps.authentication.models import Users
from ...apps.utils.mixins import AdminRequiredMixin, ProfesorRequiredMixin
from ...apps.utils.forms_date import DateInput
from django.utils.decorators import method_decorator
import os
from datetime import date, datetime


##################INSTRUMENTO ADMIN#####################
class InstruCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	template_name = 'instrumentos/crear_instrumento.html'
	model = Instrumento
	fields = ['nombr_instr']
	success_url = reverse_lazy('instrumento:list_instrumento')

######################LISTA DE INSTRUMENTOS######################
class InstruListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listainstrumento'
	model = Instrumento
	template_name = 'instrumentos/lista_instrumentos.html'

######################REPORTE DE LOS INSTRUMENTOS######################
class InstListAllView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	def get_context_data(self, **kwargs):
	    context = super(instListAllView, self).get_context_data(**kwargs)
	    context['date'] = datetime.now().strftime("%d/%m/%Y")
	    return context
	    
	context_object_name = 'ListaAllintrumentos'
	model = Instrumento
	template_name = 'reportes/report-instr-list.html'

######################ASIGNANDO INSTRUMENTO######################
class AsigInstrumentoView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	template_name = 'instrumentos/asignacion_del_alumno.html'
	model = Asignatura
	fields = ['instrumento','alumno','descripcion','fecha_entrega']
	success_url = reverse_lazy('instrumento:asig_instrumento')

######################LISTADO DE ALUMNOS######################
class AlumnoListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'ListasalumnoI'
	model = Asignatura
	template_name = 'asignacion/instrumentos_asignados.html'

class UpdateAsigAlumnView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
	template_name = 'instrumentos/update_instrumento.html'
	model = Asignatura
	fields = ['instrumento','alumno','descripcion','fecha_entrega','fecha_retiro']
	success_url = reverse_lazy('instrumento:asig_instrumento')