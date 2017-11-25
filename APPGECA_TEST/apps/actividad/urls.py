from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.actividad.views import *

urlpatterns = [

	url(r'^nueva_actividad/$', actiCreateView.as_view(),name="actividadR"),
	url(r'^listado_de_actividades/$', activListView.as_view(),name="list_actividades"),

] 
