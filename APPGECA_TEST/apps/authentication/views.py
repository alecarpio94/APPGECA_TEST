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
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.context import RequestContext
from django.conf import settings
from .models import Users, UsersManager
from APPGECA_TEST.apps.actividad.models import Actividad
from APPGECA_TEST.apps.profesor.models import Profesor
from APPGECA_TEST.apps.profesor.forms import ProfForm
from .forms import *
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.encoding import force_text
from django.shortcuts import resolve_url

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
class UsersUpdateView(LoginRequiredMixin, UpdateView):
    model = Users
    fields = ['ci' ,'first_name', 'last_name', 'email']
    template_name = 'administrador/update_user.html'
    success_url = reverse_lazy('auth:inicio')

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
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'administrador/change_password.html', {
#         'form': form
#     })
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
                a.set_password("appgeca1234")
                a.save()
                return JsonResponse({'si':'si'})
        return JsonResponse({'No':'No'})



#####################################################################
# class PasswordContextMixin(object):
#     extra_context = None

#     def get_context_data(self, **kwargs):
#         context = super(PasswordContextMixin, self).get_context_data(**kwargs)
#         context['title'] = self.title
#         if self.extra_context is not None:
#             context.update(self.extra_context)
#         return context

# class PasswordResetView(PasswordContextMixin, FormView):
#     email_template_name = 'auth/password_reset_email.html'
#     extra_email_context = None
#     form_class = PasswordResetForm
#     from_email = None
#     html_email_template_name = 'auth/password_reset_email.html'
#     subject_template_name = 'auth/password_reset_subject.txt'
#     success_url = reverse_lazy('auth:password_reset_done')
#     template_name = 'auth/password_reset_form.html'
#     title = _('Password reset')
#     token_generator = default_token_generator

#     @method_decorator(csrf_protect)
#     def dispatch(self, *args, **kwargs):
#         return super(PasswordResetView, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         opts = {
#             'use_https': self.request.is_secure(),
#             'token_generator': self.token_generator,
#             'from_email': self.from_email,
#             'email_template_name': self.email_template_name,
#             'subject_template_name': self.subject_template_name,
#             'request': self.request,
#             'html_email_template_name': self.html_email_template_name,
#             'extra_email_context': self.extra_email_context,
#         }
#         form.save(**opts)
#         return super(PasswordResetView, self).form_valid(form)


# INTERNAL_RESET_URL_TOKEN = 'set-password'
# INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'

# class PasswordResetDoneView(PasswordContextMixin, TemplateView):
#     template_name = 'auth/password_reset_done.html'
#     title = _('Password reset sent')

# class PasswordResetConfirmView(PasswordContextMixin, FormView):
#     form_class = SetPasswordForm
#     post_reset_login = False
#     post_reset_login_backend = None
#     success_url = reverse_lazy('auth:password_reset_complete')
#     template_name = 'registration/password_reset_confirm.html'
#     title = _('Enter new password')
#     token_generator = default_token_generator

#     @method_decorator(sensitive_post_parameters())
#     @method_decorator(never_cache)
#     def dispatch(self, *args, **kwargs):
#         assert 'uidb64' in kwargs and 'token' in kwargs

#         self.validlink = False
#         self.user = self.get_user(kwargs['uidb64'])

#         if self.user is not None:
#             token = kwargs['token']
#             if token == INTERNAL_RESET_URL_TOKEN:
#                 session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
#                 if self.token_generator.check_token(self.user, session_token):
#                     # If the token is valid, display the password reset form.
#                     self.validlink = True
#                     return super(PasswordResetConfirmView, self).dispatch(*args, **kwargs)
#             else:
#                 if self.token_generator.check_token(self.user, token):
#                     # Store the token in the session and redirect to the
#                     # password reset form at a URL without the token. That
#                     # avoids the possibility of leaking the token in the
#                     # HTTP Referer header.
#                     self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
#                     redirect_url = self.request.path.replace(token, INTERNAL_RESET_URL_TOKEN)
#                     return HttpResponseRedirect(redirect_url)

#         # Display the "Password reset unsuccessful" page.
#         return self.render_to_response(self.get_context_data())

#     def get_user(self, uidb64):
#         try:
#             # urlsafe_base64_decode() decodes to bytestring on Python 3
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = UserModel._default_manager.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
#             user = None
#         return user

#     def get_form_kwargs(self):
#         kwargs = super(PasswordResetConfirmView, self).get_form_kwargs()
#         kwargs['user'] = self.user
#         return kwargs

#     def form_valid(self, form):
#         user = form.save()
#         del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
#         if self.post_reset_login:
#             auth_login(self.request, user, self.post_reset_login_backend)
#         return super(PasswordResetConfirmView, self).form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super(PasswordResetConfirmView, self).get_context_data(**kwargs)
#         if self.validlink:
#             context['validlink'] = True
#         else:
#             context.update({
#                 'form': None,
#                 'title': _('Password reset unsuccessful'),
#                 'validlink': False,
#             })
#         return context

# class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
#     template_name = 'registration/password_reset_complete.html'
#     title = _('Password reset complete')

#     def get_context_data(self, **kwargs):
#         context = super(PasswordResetCompleteView, self).get_context_data(**kwargs)
#         context['login_url'] = resolve_url(settings.LOGIN_URL)
#         return context

