import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.views.generic import FormView

from core.helpers import SendEmail

from .forms import PasswordResetConfirmView, PasswordResetRequestForm, RegisterForm


class PasswordResetRequestView(FormView):
    URL = 'password_reset_request'
    template_name = 'reset_password.html'
    form_class = PasswordResetRequestForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Reset Password'
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        data = form.cleaned_data['username_or_email']
        users = User.objects.filter(Q(username=data) | Q(email=data))
        if users.exists():
            for user in users:
                SendEmail(
                    template_name='password_reset.html',
                    subject='Password reset requested',
                    to=[user.email],
                    data={
                        'domain': self.request.META['HTTP_HOST'],
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        }
                )
            messages.success(
                self.request,
                "Email on the way, if you don't receive anything,",
                "blame it on government, it's their fault"
            )
        else:
            messages.error(
                self.request,
                "Your input did not find matching user in our database"
            )
            return self.form_invalid(form)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('login')


class PasswordResetConfirmView(FormView):
    URL = 'password_reset_confirm'
    template_name = 'confirm_password.html'
    form_class = PasswordResetConfirmView

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Reset Password'
        return context

    def post(self, request, uidb64=None, token=None, *args, **kwargs):
        form = form = self.form_class(request.POST)
        if uidb64 is not None and token is not None:
            try:
                user_id = urlsafe_base64_decode(uidb64)
                user = User.objects.get(pk=user_id)
            except Exception as e:
                logging.error('Password retrieval error, ', e)
                messages.error(
                    self.request,
                    "Something is wrong with your link, try again"
                )
                return HttpResponseRedirect(self.get_success_url())
            else:
                if default_token_generator.check_token(user, token):
                    if form.is_valid():
                        post_request = self.request.POST
                        if post_request['password_confirm'] == post_request['password']:
                            user.set_password(form.cleaned_data['password'])
                            user.save()
                            return self.form_valid(form)
                        else:
                            messages.error(
                                self.request,
                                "Passwords did not match, please try again"
                            )
                            return self.form_invalid(form)
                else:
                    messages.error(self.request, "Reset password link is no longer valid")
                    return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        messages.success(self.request, "Password updated, please try now")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('login')


class UserRegistration(FormView):
    URL = 'register'
    form_class = RegisterForm
    template_name = "registration.html"


class UserLogin(View):
    URL = 'login'

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = 'Login'
        return kwargs

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        try:
            if request.user.is_authenticated:
                if (request.user.is_active and request.user.is_staff):
                    return redirect('/admin')
        except Exception:
            pass
        return render(self.request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        username = password = ''
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        try:
            login(request, user)
            if (user.is_active and user.is_staff):
                return redirect('/admin')
        except Exception as e:
            messages.error(
                request,
                'Given username and password did not match any of our records.')
            return render(request, "login.html")


class UserLogout(View):
    URL = 'logout'

    def get(self, request, *args, **kwargs):
        try:
            logout(request)
        except Exception:
            pass
        return redirect('/account/login/')
