import os
from pathlib import Path

from .django_const import INSTALLED_APPS, MIDDLEWARE
from .required_conf_section import REQUIRED_CONF_SECTIONS

# location of manage.py
BASE_DIR = str(Path(os.path.dirname(os.path.realpath(__file__))).parents[2])

# location of settings dir with conf files
SETTINGS_DIR = str(Path(os.path.dirname(os.path.realpath(__file__))).parent)

SETTINGS_PRODUCTION = 'basic_django.settings.production'
SETTINGS_DEVELOPMENT = 'basic_django.settings.development'
SETTINGS_TEST = 'basic_django.settings.test'
