from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.alumno.views import *

urlpatterns = [

	url(r'^nuevo_alumno/$', Prueba.as_view() ,name="alumnoR"),
	url(r'^listado_de_alumno/$', alumListView.as_view(),name="list_alumno"),
	url(r'^movimiento_de_alumno/$', alumMListView.as_view(),name="list_alumnoM"),
	url(r'^editar/(?P<pk>\d+)$', alumUpdateView.as_view(),name='editar_alumno'),
	url(r'^borrar_alumno/(?P<pk>\d+)$',alumDeleteView.as_view(), name='eliminar_alumno'),
	url(r'^reporte_lista_alumnos/$',alumListAllView.as_view(), name='reporte_alumnos'),

]