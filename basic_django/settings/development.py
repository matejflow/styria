import logging
import os

from .env_settings import DevelopmentSettings

config = DevelopmentSettings().load_conf()

BASE_DIR = config.BASE_DIR
SECRET_KEY = config.SECRET_KEY
DEBUG = config.DEBUG

ALLOWED_HOSTS = config.ALLOWED_HOSTS

INSTALLED_APPS = config.INSTALLED_APPS
MIDDLEWARE = config.MIDDLEWARE

LOGOUT_AT_INACTIVITY = config.LOGOUT_AT_INACTIVITY
# this will cause session expiary if uncommented, only use with LOGOUT = True
# SESSION_COOKIE_AGE = config.SESSION_COOKIE_AGE

INTERNAL_IPS = config.INTERNAL_IPS

ROOT_URLCONF = config.ROOT_URLCONF

TEMPLATES = config.TEMPLATES

WSGI_APPLICATION = config.WSGI_APPLICATION

CACHES = config.CACHES

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.DATABASE_ENGINE,
        'NAME': config.DATABASE_NAME,
        'USER': config.DATABASE_USER,
        'PASSWORD': config.DATABASE_PASSWORD,
        'HOST': config.DATABASE_HOST,
        'PORT': config.DATABASE_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
# we are not using any password validators from django

AUTH_PASSWORD_VALIDATORS = config.AUTH_PASSWORD_VALIDATORS


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = config.LANGUAGE_CODE

TIME_ZONE = config.TIME_ZONE

USE_I18N = config.USE_I18N

USE_L10N = config.USE_L10N

USE_TZ = config.USE_TZ


STATIC_URL = config.STATIC_URL
STATICFILES_DIRS = config.STATICFILES_DIRS
STATIC_ROOT = config.STATIC_ROOT

# Email settings

EMAIL_HOST = config.EMAIL_HOST
EMAIL_HOST_USER = config.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = config.EMAIL_HOST_PASSWORD
EMAIL_PORT = config.EMAIL_PORT
EMAIL_USE_TLS = config.EMAIL_USE_TLS
