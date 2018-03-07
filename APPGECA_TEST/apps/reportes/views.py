#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import CreateView 
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...apps.profesor.models import Profesor
from ...apps.instrumento.models import Asignatura
from ...apps.alumno.models import Alumno
from datetime import date, datetime
from django import http
from django.template.loader import get_template
from django.template import Context
from io import BytesIO
import cStringIO as StringIO
import cgi



# Create your views here.
def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(),content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def AlumnoPDF(request):
    alumn=Alumno.objects.all()
    return write_pdf('reportes/constancia_alumno.html',{'pagesize':'legal','alumn':alumn,})

class ListaReporteListView(LoginRequiredMixin,ListView):
	context_object_name = 'ListasalumnoR'
	model = Alumno
	second_model = Asignatura
	template_name = 'reportes/lista_constancia_alumno.html'

# class ConstanciaAlumnoDetailView(LoginRequiredMixin,DetailView):
	# def get_context_data(self, **kwargs):
	    # context = super(ConstanciaAlumnoDetailView, self).get_context_data(**kwargs)
	    # context['dia'] = datetime.now().strftime("%d")
	    # context['mes'] = datetime.now().strftime("%m")
	    # context['ano'] = datetime.now().strftime("%Y")
	    # return context

	# model = Alumno
	# template_name = 'reportes/constancia_alumno.html'

class AlumnoInstrListView(LoginRequiredMixin,DetailView):	
	def get_context_data(self, **kwargs):
	    context = super(AlumnoInstrListView, self).get_context_data(**kwargs)
	    context['dia'] = datetime.now().strftime("%d")
	    context['mes'] = datetime.now().strftime("%m")
	    context['ano'] = datetime.now().strftime("%Y")
	    return context
	model = Asignatura
	template_name = 'reportes/constancia_instrumento_alumno.html'

class ProfeConsListView(LoginRequiredMixin,DetailView):	
	def get_context_data(self, **kwargs):
	    context = super(ProfeConsListView, self).get_context_data(**kwargs)
	    context['dia'] = datetime.now().strftime("%d")
	    context['mes'] = datetime.now().strftime("%m")
	    context['ano'] = datetime.now().strftime("%Y")
	    return context

	model = Profesor
	template_name = 'reportes/constancia_trabajo.html'