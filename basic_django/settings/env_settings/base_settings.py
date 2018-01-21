import abc
import logging
import os
from pathlib import Path

from ..config_source import ConfigLoader
from ..constants import BASE_DIR, INSTALLED_APPS, MIDDLEWARE, SETTINGS_DIR


class BaseSettings(abc.ABC):

    BASE_DIR = BASE_DIR
    SETTINGS_DIR = SETTINGS_DIR
    LOG_DIR = BASE_DIR + '/log/'
    TEMP_DIR = BASE_DIR + '/tmp/'

    FILELOG_ENABLED = False
    FILELOG_LOG_LEVEL = 'error'

    LOG_FORMAT = (
        '[%(asctime)s] [file: %(filename) -16s line: %(lineno) -4d] '
        '%(levelname)-7s: %(message)s'
    )

    DEBUG = True

    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1"
        ]

    INSTALLED_APPS = INSTALLED_APPS

    MIDDLEWARE = MIDDLEWARE

    SESSION_EXPIRE_AT_BROWSER_CLOSE = False
    LOGOUT_AT_INACTIVITY = False
    SESSION_COOKIE_AGE = 10*60  # min

    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    ROOT_URLCONF = 'basic_django.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'home.context_processors.top_movies',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'basic_django.wsgi.application'

    AUTH_PASSWORD_VALIDATORS = [
    ]

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "assets"),
    ]

    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    EMAIL_USE_TLS = False

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache',
            'TIMEOUT': 60*60*24,
        }
    }

    def __init__(self):
        pass

    @abc.abstractproperty
    def config_files(self):
        """
        A list of paths to all config files that will be loaded.
        """

    @staticmethod
    def check_if_file(file_path):
        if Path(file_path).is_file():
            return str(Path(file_path))
        else:
            return False

    def load_conf(self):
        config = ConfigLoader(self).config_object
        class_name = self.__class__.__name__.replace('Settings', '')
        logging.basicConfig(
            filename=self.LOG_DIR + '{}.log'.format(class_name.lower()),
            level=getattr(logging, config.FILELOG_LOG_LEVEL.upper()),
            format=self.LOG_FORMAT,
            datefmt='%d/%m/%Y %I:%M:%S')
        return config
