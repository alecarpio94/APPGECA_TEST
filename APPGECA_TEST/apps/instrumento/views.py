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
from ...apps.instrumento.models import *
from ...apps.instrumento.forms import *
from ...apps.authentication.models import Users
from ...apps.utils.mixins import AdminRequiredMixin, ProfesorRequiredMixin
from ...apps.utils.forms_date import DateInput
from django.utils.decorators import method_decorator
import os

##################INSTRUMENTO ADMIN#####################
class instruCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	template_name = 'instrumentos/crear-instrumento.html'
	model = Instrumento
	fields = ['nombr_instr' , 'stock_min' , 'stock_max', 'uso',]
	success_url = '/listado_de_instrumento/'

class instruListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listainstrumento'
	model = Instrumento
	template_name = 'instrumentos/list-instrumentos.html'

class instListAllView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	def get_context_data(self, **kwargs):
	    context = super(instListAllView, self).get_context_data(**kwargs)
	    context['date'] = datetime.now().strftime("%d/%m/%Y")
	    return context
	    
	context_object_name = 'ListaAllintrumentos'
	model = Instrumento
	template_name = 'reportes/report-instr-list.html'