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
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q
from ...apps.actividad.models import *
from ...apps.actividad.forms import *
from ...apps.authentication.models import Users
from ...apps.utils.mixins import AdminRequiredMixin, ProfesorRequiredMixin
from ...apps.utils.forms_date import DateInput
from django.utils.decorators import method_decorator
import os

# Create your views here.

class actiCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	model = Actividad
	fields = ['codigo_act', 'nombr_acti', 'descripcio', 'fecha_inic', 'fecha_fina']
	template_name = 'actividades/crear-actividad.html'
	success_url = '/listado_de_actividades/'

class activListView(LoginRequiredMixin,ListView):
	context_object_name = 'Listasactividades'
	model = Actividad
	template_name = 'actividades/list-actividad.html'

class activCalendar(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Calendar'
	model = Actividad
	template_name = 'pagina/events.xml'