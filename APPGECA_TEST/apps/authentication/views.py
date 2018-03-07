# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.context import RequestContext
from django.conf import settings
from .models import Users, UsersManager
from APPGECA_TEST.apps.actividad.models import Actividad
from APPGECA_TEST.apps.profesor.models import Profesor
from APPGECA_TEST.apps.profesor.forms import ProfForm
from .forms import UsersModelForm, UsersUpdateModelForm
# mixins
from ...apps.utils.mixins import AdminRequiredMixin

# Create your views here.
@login_required(login_url = '/login/')
def HomeTemplateView(request):
        model = Actividad
        all_events = Actividad.objects.all()
        get_event_types = Actividad.objects.only('event_type')

        # if filters applied then get parameter and filter based on condition else return object
        if request.GET:  
            event_arr = []
            if request.GET.get('event_type') == "all":
                all_events = Actividad.objects.all()
            else:   
                all_events = Actividad.objects.filter(event_type__icontains=request.GET.get('event_type'))

            for i in all_events:
                event_sub_arr = {}
                event_sub_arr['title'] = i.nombr_acti
                start_date = datetime.datetime.strptime(str(i.fecha_inic.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                end_date = datetime.datetime.strptime(str(i.fecha_fina.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                event_sub_arr['start'] = start_date
                event_sub_arr['end'] = end_date
                event_arr.append(event_sub_arr)
            return HttpResponse(json.dumps(event_arr))

        context = {
            "Actividad":all_events,
            "get_event_types":get_event_types,

        }
        return render(request,'administrador/index.html',context)


###########LOGIN###########
class LoginView(View):
    form_class = AuthenticationForm
    template_name = "login/page-login.html"
    mensaje = ""

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'message': ''})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redirect
                url_next = request.GET.get('next')
                if url_next is not None:
                    return redirect(url_next)
                else:
                    #return redirect(reverse_lazy('eventos:list'))
                    mensaje = "Bienvenido Nuevamente!"
                    return render(request,'login/preloader.html', {'message': mensaje})
            else:
                return reverse_lazy('auth:ERROR_404')
        else:
            mensaje ="Por favor, ingrese la cedula y la clave correctos."
        return render(request, self.template_name, {'form': self.form_class, 'message': mensaje})

###############################CREAR USUARIO###############################
class UsersCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Users
    form_class = UsersModelForm
    template_name = 'administrador/users_form.html'
    success_url = reverse_lazy('auth:list')

##########################LISTADO DE PROFESORES ACTIVOS/INACTIVOS##########################
class ProfesorListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Profesor
    template_name = 'administrador/activar_profesor.html'

##############################LISTA DE USUARIOS##############################
class UsersListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    context_object_name = 'list_user'
    model = Users
    template_name = 'administrador/lista_Users.html'

###############################ACTUALIZAR EL USUARIO###############################
class UsersUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Users
    fields = ['ci' ,'first_name', 'last_name', 'email','is_active','password','password']
    template_name = 'administrador/users_form.html'

    def get_success_url(self):
        return reverse_lazy('auth:list', args=(self.user.pk))

###############################ELIMNIAR EL USUARIO###############################
class UsersDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Users
    template_name = 'administrador/user_confirm_delete.html'
    success_url = reverse_lazy('auth:list')

# logout
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')

###############################PAGE 404###############################
class error404(TemplateView):
    template_name = 'login/page-error.html'

#########################CAMBIAR PASSWORD#############################    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'administrador/change_password.html', {
        'form': form
    })
######################################################################
class GuardarPermiso(View):
    model = Users

    def post(self, *args, **kwargs):
        cedula1 = self.request.POST.get('cedu1')
        cedula2 = self.request.POST.get('cedu2')
        if cedula1 == cedula2:
            profesor = Profesor.objects.filter(cedula_profesor=cedula1).first()
            if profesor:
                a = self.model(ci=cedula1, is_staff=True, is_profesor=True, first_name=profesor.nombre_profesor, last_name=profesor.apellido_profesor)
                a.set_password("hola1234")
                a.save()
                return JsonResponse({'si':'si'})
        return JsonResponse({'No':'No'})