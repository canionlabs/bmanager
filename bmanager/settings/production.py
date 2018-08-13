from .base import *

from prettyconf import config
import dj_database_url


DEBUG = config("DEBUG", default=False, cast=config.boolean)

ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}