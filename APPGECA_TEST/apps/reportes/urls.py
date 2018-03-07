from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.reportes.views import *

urlpatterns = [

	url(r'^lista_alumnos/$',ListaReporteListView.as_view(), name='reporte_alumnos'),

	url(r'^constancia_alumnos/',AlumnoPDF, name='constan_alumnos'),
	
	url(r'^constancia_instrumento/(?P<pk>\d+)$', AlumnoInstrListView.as_view(),name="const_asign"),

	url(r'^constancia_profesor/(?P<pk>\d+)$', ProfeConsListView.as_view(),name="const_trab"),

]
