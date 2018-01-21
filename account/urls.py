from django.conf.urls import url

from .views import (
    PasswordResetConfirmView, PasswordResetRequestView, UserLogin, UserLogout, UserRegistration
)

urlpatterns = [
    url(r'login/$', UserLogin.as_view(), name=UserLogin.URL),
    url(r'logout/$', UserLogout.as_view(), name=UserLogout.URL),
    url(r'register/$', UserRegistration.as_view(), name=UserRegistration.URL),
    url(
        r'reset_password$',
        PasswordResetRequestView.as_view(),
        name=PasswordResetRequestView.URL
    ),
    url(
        r'reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(),
        name=PasswordResetConfirmView.URL
    ),
]
