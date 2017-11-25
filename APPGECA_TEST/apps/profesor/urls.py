from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.profesor.views import *

urlpatterns = [

	url(r'^nuevo_profesor/$', profCreateView.as_view(), name = 'profesorR'),
	url(r'^listado_de_profesor/$', profListView.as_view(),name="list_profesor"),
	url(r'^movimiento_de_profesor/$', profMListView.as_view(),name="list_profesorM"),
	url(r'^editarP/(?P<pk>\d+)$', profUpdateView.as_view(),name='editar_profesor'),
	url(r'^borrar_profesor/(?P<pk>\d+)$',profDeleteView.as_view(), name='eliminar_profesor'),
	url(r'^reporte_lista_profesores/$',profListAllView.as_view(), name='reporte_profesor'),

] 
