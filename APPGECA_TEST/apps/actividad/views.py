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
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView,UpdateView,DeleteView
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q
from ...apps.actividad.models import *
from ...apps.actividad.forms import *
from ...apps.authentication.models import Users
from ...apps.utils.mixins import AdminRequiredMixin
from ...apps.utils.forms_date import DateInput
from django.utils.decorators import method_decorator
import os

# Create your views here.
######################CREAR ACTIVIDAD######################
class ActiCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	model = Actividad
	fields = ['nombr_acti', 'descripcio', 'fecha_inic','hora_inico', 'hora_final' ,'fecha_fina','status1']
	template_name = 'actividad/crear_actividad.html'
	success_url = reverse_lazy('actividad:list_actividades')
	mensaje = ""

	def form_valid(self, form):
		p = form.save(commit=False)
		fecha = p.fecha_inic
		fecha_dada = p.fecha_fina
		horaI = p.hora_inico
		horaF = p.hora_final
		if fecha_dada >= fecha:
			if horaF >= horaI:
				print ("Si Paso")
				return super(ActiCreateView, self).form_valid(form)
			else:
				self.mensaje = "La hora seleccionada no es valida"
				return render(self.request,'actividad/crear_actividad.html', {'form':form, 'mensaje':self.mensaje})
		else:
			self.mensaje = "La fecha seleccionada no es valida"
			return render(self.request,'actividad/crear_actividad.html', {'form':form, 'mensaje':self.mensaje})
			
######################LISTA DE ACTIVIDADES######################
class ActivListView(LoginRequiredMixin,ListView):
	context_object_name = 'Listasactividades'
	model = Actividad
	template_name = 'actividad/lista_de_actividades.html'

class ActivUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
	template_name = 'actividad/actualizar_actividad.html'
	model = Actividad
	fields = ['nombr_acti', 'descripcio', 'fecha_inic','hora_inico', 'hora_final', 'fecha_fina', 'status1', 'status2','status3']
	success_url = reverse_lazy('actividad:list_actividades')
	
class ActivDeleteView(LoginRequiredMixin,AdminRequiredMixin, DeleteView):
	
	model = Actividad
	template_name = 'actividad/actividad_confirm_delete.html'
	success_url = reverse_lazy('actividad:list_actividades')

######################CALENDARIO DE ACTIVIDADES######################
def event(request):
	
	all_events = Actividad.objects.all()
	get_event_types = Actividad.objects.only('event_type')

	# if filters applied then get parameter and filter based on condition else return object
	if request.GET:  
	    event_arr = []
	    if request.GET.get('event_type') == "all":
	        all_events = Actividad.objects.all()
	    else:   
	        all_events = Actividad.objects.filter(event_type__icontains=request.GET.get('event_type'))

	    for i in all_events:
	        event_sub_arr = {}
	        event_sub_arr['title'] = i.nombr_acti
	        start_date = datetime.datetime.strptime(str(i.fecha_inic.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
	        end_date = datetime.datetime.strptime(str(i.fecha_fina.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
	        event_sub_arr['start'] = start_date
	        event_sub_arr['end'] = end_date
	        event_arr.append(event_sub_arr)
	    return HttpResponse(json.dumps(event_arr))

	context = {
	    "Actividad":all_events,
	    "get_event_types":get_event_types,

	}
	return render(request,'pagina/calendario.html',context)
