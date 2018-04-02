from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import *
# Register your models here.

admin.site.register(Profesor)
admin.site.register(Asignados)
admin.site.register(Evaluado)
admin.site.register(PersonalAdmin)
admin.site.register(PersonalObrero)
