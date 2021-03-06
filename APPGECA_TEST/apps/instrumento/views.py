
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
	mensaje = ""
	
	# def form_valid(self, form):
	# 	forma = form_valid.save(commit=False)
	# 	if forma:
	# 		mensaje = "GUARDADO"
	# 		return super(InstruCreateView, self.mensaje).form_valid(form)
	# 	else:
	# 		mensaje = "ERROR"
	# 		return render(self.request, self.template_name, {'form':form, 'mensaje':mensaje})

######################LISTA DE INSTRUMENTOS######################
class InstruListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'Listainstrumento'
	model = Instrumento
	template_name = 'instrumentos/lista_instrumentos.html'

######################ASIGNANDO INSTRUMENTO######################
from ...apps.profesor.models import Asignados
class AsigInstrumentoView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	template_name = 'instrumentos/asignacion_del_alumno.html'
	model = Asignatura
	fields = ['instrumento','alumno','descripcion','fecha_entrega']
	success_url = reverse_lazy('instrumento:asig_instrumento')
	mensaje = ""

	def form_valid(self, form):
		alumno = form.save(commit=False)
		halumno = Asignados.objects.filter(alumno=alumno.alumno.pk).first()
		if halumno:
			if alumno.instrumento.pk == halumno.profesor.asignacion.pk:
				return super(AsigInstrumentoView, self).form_valid(form)
			else:
				self.mensaje = "Lo siento el alumno no debe tener el instrumento {}".format(alumno.instrumento.nombr_instr)
				return render(self.request, self.template_name, {'form':form, 'mensaje':self.mensaje})
		else:
			self.mensaje = "Lo siento el alumno no tiene docente asignado"
			return render(self.request, self.template_name, {'form':form, 'mensaje':self.mensaje})

######################LISTADO DE ALUMNOS######################
class AlumnoListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'ListasalumnoI'
	model = Asignatura
	template_name = 'asignacion/instrumentos_asignados.html'

class DeleteAsigAlumnView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
	model = Asignatura
	template_name = 'instrumentos/update_instrumento.html'
	success_url = reverse_lazy('instrumento:asig_instrumento')