from .base import *
import os


DEBUG = config("DEBUG", default=True, cast=config.boolean)

ALLOWED_HOSTS = ['*']

DEV_APPS = []

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS

DATABASES['default'] = dj_database_url.parse('sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))