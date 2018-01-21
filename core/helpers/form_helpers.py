from django.contrib.auth.models import User


class UniqueUserEmail():
    """
    Need to check if email is unique, this should not be done on User module
    because that would mean on each server deployment we would have to
    manually change User model
    """

    def clean(self):
        email = self.cleaned_data.get('email')
        user_id = self.cleaned_data.get('identifier')
        if email and User.objects.filter(email=email).exclude(pk=user_id).count():
            self = add_field_error(self, 'email', 'Email must be unique!')


def add_field_error(form, field, message):
    if field in form.errors:
        form.errors[field].append(message)
    else:
        form.errors[field] = form.error_class([message])
    return form
