from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.actividad.views import *

urlpatterns = [

	url(r'^nueva_actividad/$', ActiCreateView.as_view(),name="actividadR"),
	url(r'^listado_de_actividades/$', ActivListView.as_view() ,name="list_actividades"),
	url(r'^editar_actividad/(?P<pk>\d+)$', ActivUpdateView.as_view(),name='editar_acti'),
	url(r'^eliminar/(?P<pk>\d+)$', ActivDeleteView.as_view(),name='eliminar_acti'),
    url(r'^cronograma/', event),


] 
