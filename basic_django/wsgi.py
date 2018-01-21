"""
WSGI config for basic_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from .settings.constants import SETTINGS_PRODUCTION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_PRODUCTION)

application = get_wsgi_application()
