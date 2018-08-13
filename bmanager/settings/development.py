from .base import *
import os

DEBUG = config("DEBUG", default=True, cast=config.boolean)

ALLOWED_HOSTS = ['*']

DEV_APPS = []

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}