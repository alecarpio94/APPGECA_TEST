# -*- coding: utf-8 -*-
from django.contrib.auth import views as auth_views

from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib import admin

from APPGECA_TEST.apps.authentication import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth

urlpatterns = [

	##############################################################
	url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^registrar/$', views.UsersCreateView.as_view(), name='add'),
    url(r'^activacion/$', views.ProfesorListView.as_view(), name='pro_activate'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

	##############################################################
    url(r'^list_user/$', views.UsersListView.as_view(), name='list'),
    url(r'^editar/2sdfg3(?P<pk>\d+)54sdfg5/$',views.UsersUpdateView.as_view(), name='update'),
    url(r'^eliminar/h43k(?P<pk>[-\ \w]+)m4n5/$',views.UsersDeleteView.as_view(), name='delete'),

	##############################################################
	url(r'^accounts/login/$', views.error404.as_view(),name="ERROR_404"),

    url(
        r'^password/recovery/$',
        auth_views.PasswordResetView.as_view(
            template_name='auth/password_reset_form.html',
            html_email_template_name='auth/password_reset_email.html',
        ),
        name='password_reset',
    ),

    url(
        r'^password/recovery/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html',
        ),
        name='password_reset_done',
    ),

    url(
        r'^password/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('home'),
            post_reset_login=True,
            template_name='auth/password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),

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
