from django.conf.urls import url
from ...apps.inicio import views

import views

urlpatterns = [

    url(r'^Clarinete/', views.catedra4),
    url(r'^Percusion/', views.catedra2),
    url(r'^Guitarra/', views.catedra3),  
    url(r'^contacto/', views.contact),
    url(r'^preguntas/', views.frecuente),
    url(r'^quienes_somos/', views.somos),
    url(r'^mision_vision/', views.mision),
    url(r'^cronograma/', views.calendario),

    url(r'^', views.inicio),  
] 
