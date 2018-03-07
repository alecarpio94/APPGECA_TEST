#!/usr/bin/python   
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import AccessMixin
from ..authentication.models import Users

class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)

class ProfesorRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_profesor:
            return super(ProfesorRequiredMixin, self).dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
