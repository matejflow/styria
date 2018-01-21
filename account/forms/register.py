from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.helpers import UniqueUserEmail


class RegisterForm(UserCreationForm, UniqueUserEmail):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'email',
            'username',
            )
