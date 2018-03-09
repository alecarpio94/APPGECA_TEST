from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.reportes.views import *

urlpatterns = [

	url(r'^lista_alumnos/$',ListaReporteListView.as_view(), name='reporte_alumnos'),

	url(r'^constancia_alumnos/(?P<pk>[-\ \w]+)',AlumnoPDF.as_view(), name='constan_alumnos'),
	
	url(r'^constancia_instrumento/(?P<pk>[-\ \w]+)$', AlumnoInstrumentoPDF.as_view(),name="const_asign"),

	url(r'^constancia_profesor/(?P<pk>[-\ \w]+)$', ProfesorPDF.as_view(),name="const_trab"),

	url(r'^reporte_lista_alumnos/$',ListaAlumnosPDF.as_view(), name='reporte_alumnos'),

	url(r'^reporte_lista_profesores/$',ListaProfesoresPDF.as_view(), name='reporte_profesor'),

	url(r'^reporte_lista_instrumentos/$',ListaInstrumentosPDF.as_view(), name='reporte_instrumentos'),
]
