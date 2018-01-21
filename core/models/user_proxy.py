from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class UserProxyQuerySet(models.QuerySet):
    def find_user_by_email_username_email(self, data):
        if data:
            return self.filter(
                Q(email__icontains=data) |
                Q(username__icontains=data) |
                Q(last_name__icontains=data)
            )
        return self

    def by_status(self, data):
        if (data and not data == "all"):
            return self.filter(is_active=data)
        return self

    def by_role(self, data):
        if (data and not data == "all"):
            if data == 'superuser':
                return self.filter(Q(is_superuser=True))
            elif data == 'staff':
                return self.filter(Q(is_staff=True) & Q(is_superuser=False))
            else:
                return self.filter(Q(is_staff=False) & Q(is_superuser=False))
        return self


class UserProxy(User):
    def activate(self):
        self.is_active = True
        return self

    def deactivate(self):
        self.is_active = False
        return self

    objects = UserProxyQuerySet.as_manager()

    class Meta:
        proxy = True
