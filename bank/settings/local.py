from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOW_CREDENTIALS = True

# URLS PARA PERMITIDAS PARA REALIZAR PETICIONES
CORS_ALLOWED_ORIGINS = [
	'http://localhost:4200',
	'http://127.0.0.1:4200'
]

# URLS PARA PERMITIDAS PARA POST
CSRF_TRUSTED_ORIGINS = [
	'http://localhost:4200',
	'http://127.0.0.1:4200'
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'hipoo_db',
		'USER': 'hipoo_us',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '5432'
	}
}