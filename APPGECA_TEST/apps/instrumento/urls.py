from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.instrumento.views import *

urlpatterns = [

	url(r'^nuevo_instrumento/$', instruCreateView.as_view(),name="instrumentoR"),
	url(r'^listado_de_instrumento/$', instruListView.as_view(),name="list_instrumento"),
	url(r'^reporte_lista_instrumentos/$',instListAllView.as_view(), name='reporte_instrumentos'),

]