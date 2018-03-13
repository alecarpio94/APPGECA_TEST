#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic import CreateView 
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...apps.profesor.models import Profesor
from ...apps.alumno.models import Alumno
from ...apps.instrumento.models import *
from datetime import date, datetime
from django import http
from io import BytesIO
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string
from xhtml2pdf import pisa

# Create your views here.
def write_pdf(template, context):
    html  = render_to_string(template, context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(),content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


#####################################################################################
class AlumnoPDF(LoginRequiredMixin,View):
	def get(self, *args, **kwargs):	
		date = datetime.now()
		alumn = Alumno.objects.filter(pk=self.kwargs['pk']).first()
		return write_pdf('reportes/constancia_alumno.html',{'alumn':alumn, 'date':date,'request':self.request})

#####################################################################################
class AlumnoInstrumentoPDF(LoginRequiredMixin,View):
	def get(self, *args, **kwargs):
		asig = Asignatura.objects.filter(alumno=self.kwargs['pk']).first()
		if asig:
			return write_pdf('reportes/constancia_instrumento_alumno.html', {'asignatura':asig ,'request':self.request})
		else:
			return render(self.request,'reportes/error404.html')

#####################################################################################
class ProfesorPDF(LoginRequiredMixin,View):
	def get(self, *args, **kwargs):
		prof = Profesor.objects.filter(pk=self.kwargs['pk']).first()
		return write_pdf('reportes/constancia_trabajo.html',{'prof':prof, 'request':self.request})
		

#####################################################################################
class ListaReporteListView(LoginRequiredMixin,ListView):
	context_object_name = 'ListasalumnoR'
	model = Alumno
	second_model = Asignatura
	template_name = 'reportes/lista_constancia_alumno.html'

#####################################################################################
class ListaAlumnosPDF(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		alumno = Alumno.objects.all()
		return write_pdf('reportes/report-alumn-list.html', {'alumno':alumno})

#####################################################################################
class ListaProfesoresPDF(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		profesor = Profesor.objects.all()
		return write_pdf('reportes/report-prof-list.html', {'profesor':profesor})

#####################################################################################
class ListaInstrumentosPDF(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		instrumento = Instrumento.objects.all()
		return write_pdf('reportes/report-instr-list.html', {'instrumento':instrumento})

class ManualPDF(LoginRequiredMixin, View):
	HttpResponseRedirect('reportes/manual_de_usuario.pdf')		