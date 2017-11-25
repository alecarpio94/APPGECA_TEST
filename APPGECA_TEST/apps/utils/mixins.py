from django.contrib.auth.mixins import AccessMixin

class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.is_secretaria:
            return self.handle_no_permission()
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)

class ProfesorRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_profesor:
            return super(ProfesorRequiredMixin, self).dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
