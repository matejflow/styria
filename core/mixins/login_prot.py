from django.contrib import messages
from django.shortcuts import redirect


class LoginMixin:
    """User area only"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Please login to get access')
            return redirect('login')
        if not request.user.is_active:
            messages.error(request, 'Your account is not active')
            try:
                return redirect(request.META['HTTP_REFERER'])
            except KeyError:
                return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class StaffLoginMixin(LoginMixin):
    """Protects admin views for staff (superuser is also staff) members"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, 'You don\'t have permission to access that area')
            try:
                return redirect(request.META['HTTP_REFERER'])
            except KeyError:
                return redirect('login')

        return super().dispatch(request, *args, **kwargs)


class SuperUserOnlyMixin(StaffLoginMixin):
    """Gives access to superuser only"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'You don\'t have permission to access that area')
            try:
                return redirect(request.META['HTTP_REFERER'])
            except KeyError:
                return redirect('admin_index')

        return super().dispatch(request, *args, **kwargs)
