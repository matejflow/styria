import logging
import os

from .env_settings import DevelopmentSettings

configure = DevelopmentSettings().load_conf()

BASE_DIR = configure.BASE_DIR
SECRET_KEY = configure.SECRET_KEY
DEBUG = configure.DEBUG

ALLOWED_HOSTS = configure.ALLOWED_HOSTS

INSTALLED_APPS = configure.INSTALLED_APPS
MIDDLEWARE = configure.MIDDLEWARE

SESSION_EXPIRE_AT_BROWSER_CLOSE = configure.SESSION_EXPIRE_AT_BROWSER_CLOSE
LOGOUT_AT_INACTIVITY = configure.LOGOUT_AT_INACTIVITY
SESSION_COOKIE_AGE = configure.SESSION_COOKIE_AGE

INTERNAL_IPS = configure.INTERNAL_IPS

ROOT_URLCONF = configure.ROOT_URLCONF

TEMPLATES = configure.TEMPLATES

WSGI_APPLICATION = configure.WSGI_APPLICATION

DATABASES = {
    'default': {
        'ENGINE': configure.DATABASE_ENGINE,
        'NAME': configure.DATABASE_NAME,
        'USER': configure.DATABASE_USER,
        'PASSWORD': configure.DATABASE_PASSWORD,
        'HOST': configure.DATABASE_HOST,
        'PORT': configure.DATABASE_PORT,
    }
}

AUTH_PASSWORD_VALIDATORS = configure.AUTH_PASSWORD_VALIDATORS


LANGUAGE_CODE = configure.LANGUAGE_CODE

TIME_ZONE = configure.TIME_ZONE

USE_I18N = configure.USE_I18N

USE_L10N = configure.USE_L10N

USE_TZ = configure.USE_TZ


STATIC_URL = configure.STATIC_URL
STATICFILES_DIRS = configure.STATICFILES_DIRS
STATIC_ROOT = configure.STATIC_ROOT

# Email settings

EMAIL_HOST = configure.EMAIL_HOST
EMAIL_HOST_USER = configure.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = configure.EMAIL_HOST_PASSWORD
EMAIL_PORT = configure.EMAIL_PORT
EMAIL_USE_TLS = configure.EMAIL_USE_TLS
