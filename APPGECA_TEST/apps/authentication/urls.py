# -*- coding: utf-8 -*-
from django.contrib.auth import views as auth_views

from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from django.contrib.auth.views import (
    password_reset, 
    password_reset_done, 
    password_reset_confirm, 
    password_reset_complete
    )
from APPGECA_TEST.apps.authentication import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth
# from django.contrib.auth.views import password_reset, password_reset_done

urlpatterns = [

	##############################################################
	url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^registrar/$', views.UsersCreateView.as_view(), name='add'),
    url(r'^activacion/$', views.ProfesorListView.as_view(), name='pro_activate'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

	##############################################################
    url(r'^list_user/$', views.UsersListView.as_view(), name='list'),
    url(r'^actualizar/2sdfg3(?P<pk>\d+)54sdfg5/$',views.UsersUpdateView.as_view(), name='update'),
    url(r'^eliminar/h43k(?P<pk>[-\ \w]+)m4n5/$',views.UsersDeleteView.as_view(), name='delete'),

	##############################################################
	url(r'^accounts/login/$', views.error404.as_view(),name="ERROR_404"),

    ##########################RESTAURAR CONTRASEÑA##########################

    url(r'^reset/password_reset', password_reset, 
        {'template_name':'auth/password_reset_form.html',
        'email_template_name': 'auth/password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', password_reset_done, 
        {'template_name': 'auth/password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
        {'template_name': 'auth/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    # url(r'^reset/done',password_reset_complete,{'template_name':'auth/password_reset_complete.html'},
        # name='password_reset_complete'),
    url(r'^reset/done',password_reset_complete,{'template_name':'auth/password_reset_complete.html'},name='password_reset_complete'),

    # url(r'^password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)/(?P<token>.+)/$$',
    #     views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # url(r'^reset/fin/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    ##########################CAMBIO DE CONTRASEÑA##########################
    url(
        r'^password_update/$',
        auth_views.password_change,
        {
            'template_name': 'auth/password_change_form.html',
            'post_change_redirect': 'auth:auth_password_change_done',
        },
        name='auth_password_change',
    ),

    url(
        r'^password_update_done/$',
        auth_views.password_change_done,
        {
            'template_name': 'auth/password_change_done.html',
        },
        name='auth_password_change_done',
    ),
	##############################################################
	url(r'^bienvenido/', views.HomeTemplateView, name="inicio"),

	url(r'^guardar/', views.GuardarPermiso.as_view(), name="permiso"),
]
