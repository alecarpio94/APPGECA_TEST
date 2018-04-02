#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...apps.profesor.models import *
from ...apps.alumno.models import Alumno
from ...apps.instrumento.models import *
from datetime import date, datetime
from django import http
from io import BytesIO
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string
from xhtml2pdf import pisa
#import pypdf2

# Create your views here.
def write_pdf(template, context):
    html  = render_to_string(template, context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(),content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))

# @login_required()
# def PDFREAD(request):
# 	pdf_file = open('reportes/manual_de_usuario.pdf')
# 	read_pef = PyPDF2.PdfFileRead(pdf_file)

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
			return write_pdf('reportes/constancia_instrumento_alumno.html', {'asignatsura':asig ,'request':self.request})
		else:
			return render(self.request,'reportes/error404.html')

#####################################################################################
class ListaAlumnoInstrumentoPDF(LoginRequiredMixin,View):
	def get(self, *args, **kwargs):
		asignado = Asignatura.objects.filter(instrumento=self.kwargs['pk'])
		return write_pdf('reportes/constancia_instrumentos.html', {'asignados':asignado , 'instrumento': self.kwargs['pk'],'request':self.request})


#####################################################################################
class ProfesorPDF(LoginRequiredMixin,View):
	def get(self, *args, **kwargs):
		prof = Profesor.objects.filter(pk=self.kwargs['pk']).first()
		return write_pdf('reportes/constancia_trabajo.html',{'prof':prof, 'request':self.request})
		
#####################################################################################
class EvaluacionAlumnoPDF(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		evaluados = Evaluado.objects.filter(asignados=self.kwargs['pk'])
		return write_pdf('reportes/constancia_evaluacion_individual.html', {'evaluados':evaluados, 'request':self.request})

#####################################################################################
class ListaAlumnoProfesor(LoginRequiredMixin, ListView):
	def get(self, *args,**kwargs):
	    user_login = self.request.user
	    profesor = Profesor
	    if user_login:
	    	profesor_login = user_login.ci
	    	profesor = Profesor.cedula_profesor
	    	if profesor_login:
	    		if profesor:
		    		alumnos_profesor = Asignados.objects.filter(profesor = profesor_login)
		    		if alumnos_profesor:
		    			return write_pdf('reportes/lista_alumnos_profesor.html', {'object_list':alumnos_profesor, 'request':self.request})
		    		else:
	    				return HttpResponse('Nada')
    			else:	
    				return HttpResponse('Nada')
	    	else:
	    		return HttpResponse('Nada')
	    else:
	    	return HttpResponse('Nada')
	    return HttpResponse('Nada')

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

####################################################################################
class ListaPersonalAdministrativoPDF(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		personal = PersonalAdmin.objects.all()
		return write_pdf('reportes/listado_personal_adminstrativo.html', {'personal':personal})

####################################################################################
class ListaPersonalObreroPDF(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		personal = PersonalObrero.objects.all()
		return write_pdf('reportes/listado_personal_obrero.html', {'personal':personal})

#####################################################################################
class ListaInstrumentosPDF(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		instrumento = Instrumento.objects.all()
		return write_pdf('reportes/report-instr-list.html', {'instrumento':instrumento})
from django.core.files.storage import FileSystemStorage

class ManualPDF(View):
	def get(self, *args, **kwargs):
		fs = FileSystemStorage()
		filename = 'manual_de_usuario.pdf'
		with fs.open(filename) as pdf:
			response = HttpResponse(pdf)
			response['Content-type'] = 'application/pdf'
			#response['Content-Disposition'] = 'inline:filename=manual_de_usuario.pdf'			
		return response
		

