from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOW_CREDENTIALS = True

# URLS PARA PERMITIDAS PARA REALIZAR PETICIONES
CORS_ALLOWED_ORIGINS = []

# URLS PARA PERMITIDAS PARA POST
CSRF_TRUSTED_ORIGINS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}