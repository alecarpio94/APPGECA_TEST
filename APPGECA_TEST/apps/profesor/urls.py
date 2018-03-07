from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.profesor.views import *

urlpatterns = [

	url(r'^nuevo_profesor/$', ProfCreateView.as_view(), name = 'profesorR'),
	url(r'^actualizar_profesor/(?P<pk>\d+)$', ProfUpdateView.as_view(),name='editar_profesor'),
	url(r'^borrar_profesor/(?P<pk>\d+)$',ProfDeleteView.as_view(), name='eliminar_profesor'),
	url(r'^retiro/(?P<pk>\d+)$',RetiroAlumnoView.as_view(), name='retiro_alumno'),

	url(r'^listado_de_profesor/$', ProfListView.as_view(),name="list_profesor"),
	url(r'^alumno_asignados/$', ProfAlumListView.as_view(),name="list_alumn"),
	
	url(r'^evaluar/$', EvaAlumListView.as_view(),name="eva_alumn"),
	
	url(r'^asignando_alumno/$', AlumAsigView.as_view(),name="asig_alumn"),
	
	url(r'^asignados/$',AsigAlumListView.as_view(), name='alumno_profesor'),

	url(r'^reporte_lista_profesores/$',ProfListAllView.as_view(), name='reporte_profesor'),


] 
