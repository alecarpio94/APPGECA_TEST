from django.conf.urls import url
from ...apps.instrumento.views import *

urlpatterns = [

	url(r'^nuevo_instrumento/$', InstruCreateView.as_view(),name="instrumentoR"),
	url(r'^listado_de_instrumento/$', InstruListView.as_view(),name="list_instrumento"),

	url(r'^alumno_listado/$', AlumnoListView.as_view(),name="asig_instrumento"),
	url(r'^asignacion_instrumento/$', AsigInstrumentoView.as_view(),name="asign_alumno"),
	
	url(r'^editarA/(?P<pk>\d+)$', UpdateAsigAlumnView.as_view(), name="retir_instr"),

	url(r'^reporte_lista_instrumentos/$',InstListAllView.as_view(), name='reporte_instrumentos'),

]