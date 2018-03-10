"""APPGECA_TEST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # url(r'^', include('django.contrib.auth.urls',namespace='pass')),
    ##################################################################################
    url(r'^', include('APPGECA_TEST.apps.actividad.urls', namespace='actividad')),
    url(r'^', include('APPGECA_TEST.apps.alumno.urls', namespace='alumno')),
    url(r'^', include('APPGECA_TEST.apps.profesor.urls', namespace='profesor')),
    url(r'^', include('APPGECA_TEST.apps.instrumento.urls', namespace='instrumento')),
    url(r'^', include('APPGECA_TEST.apps.reportes.urls', namespace='reportes')),
    ##################################################################################
    url(r'^', include('APPGECA_TEST.apps.authentication.urls', namespace='auth')),
    url(r'^', include('APPGECA_TEST.apps.inicio.urls', namespace='inicio')),
    ##################################################################################

]