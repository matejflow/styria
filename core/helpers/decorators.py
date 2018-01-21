from django.core.exceptions import PermissionDenied


def superuser_only(func):
    """
    Limit actions to superuser only
    """

    def _inner(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied
        return func(self, *args, **kwargs)
    return _inner
