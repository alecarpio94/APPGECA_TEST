from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.alumno.views import *

urlpatterns = [

	url(r'^nuevo_alumno/$', Prueba.as_view() ,name="alumnoR"),
	url(r'^listado_de_alumno/$', AlumListView.as_view(),name="list_alumno"),
	url(r'^editar/(?P<pk>\d+)$', AlumUpdateView.as_view(),name='update_alumno'),
	url(r'^borrar_alumno/(?P<pk>\d+)$',AlumDeleteView.as_view(), name='eliminar_alumno'),
	
	url(r'^reporte_lista_alumnos/$',AlumListAllView.as_view(), name='reporte_alumnos'),

	url(r'^datos_del_alumno/(?P<pk>\d+)$',AlumnAllListView.as_view(), name='data_alumnos'),

]