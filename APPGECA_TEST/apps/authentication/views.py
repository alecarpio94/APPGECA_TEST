# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.conf import settings
from .models import Users
from .forms import UsersModelForm, UsersUpdateModelForm
# mixins
from ...apps.utils.mixins import AdminRequiredMixin,ProfesorRequiredMixin

# Create your views here.
class HomeTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'administrador/index.html'

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login/page-login.html", { 'form': form })

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/bienvenido/') 
            else:
                return render(request,"administrador/page-error.html")
        else:
            return redirect('/login/')
        return render(request)

class UsersCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Users
    form_class = UsersModelForm
    template_name = 'login/users_form.html'

class UsersListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    context_object_name = 'list_user'
    model = Users
    template_name = 'administrador/listUsers.html'

class UsersUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    template_name = 'administrador/update_user.html'
    model = Users
    fields = ['username','first_name','last_name','email']
    exclude = ('created_at', 'updated_at', 'groups', 'user_permissions',
            'last_login', 'is_active', 'date_joined', 'password')
    success_url = '/list_user/'

class UsersUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Users
    form_class = UsersUpdateModelForm

    def get_success_url(self):
        return reverse_lazy('auth:list_user', args=(self.object.pk,))


class UsersDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    
    model = Users
    template_name = 'administrador/user_confirm_delete.html'
    success_url = reverse_lazy('auth:list')

# logout
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')

class error404(TemplateView):
    template_name = 'administrador/page-error.html'
