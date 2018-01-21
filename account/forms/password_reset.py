from django import forms


class PasswordResetRequestForm(forms.Form):
    username_or_email = forms.CharField(required=True, min_length=4)


class PasswordResetConfirmView(forms.Form):
    password = forms.CharField(required=True, min_length=8)
    password_confirm = forms.CharField(required=True, min_length=8)
