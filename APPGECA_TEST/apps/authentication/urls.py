from django.conf.urls import url
from ...apps.authentication.views import *


import views

urlpatterns = [

	##############################################################
	url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^add/$', UsersCreateView.as_view(), name='add'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
	##############################################################
    url(r'^list_user/$', UsersListView.as_view(), name='list'),
	url(r'^update_user/(?P<pk>\d+)$', UsersUpdateView.as_view(),name='update'),
	##############################################################
	url(r'^accounts/login/$', error404.as_view(),name="ERROR_404"),
	##############################################################
	url(r'^bienvenido/', HomeTemplateView.as_view()),
] 


