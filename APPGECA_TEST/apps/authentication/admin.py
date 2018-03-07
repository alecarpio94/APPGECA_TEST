from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import *

# Register your models here.
# admin.site.register(Account)
@admin.register(Users)
class User(UserAdmin):
    list_display = ('ci','ci_profesor' ,'is_staff','is_secretaria','is_profesor','is_alumno','is_active','is_staff','is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_secretaria','is_profesor','is_alumno','is_active', 'groups')
    search_fields = ('username', 'ci', 'is_secretaria','is_profesor','is_alumno','first_name', 'last_name', 'email')
    ordering = ('ci',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('ci', 'password')  }),
        (_('Personal info'), {'fields': ('ci' ,'first_name', 'last_name', 'email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_secretaria','is_profesor','is_alumno',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username' ,'ci', 'ci_profesor' ,'first_name', 'last_name','is_secretaria','is_profesor','is_alumno' ,'is_active','is_staff','is_superuser' ,'email','password1', 'password2'),
        }),
    )
