from .base import *

DEBUG = False

ALLOWED_HOSTS = ["your-domain.com"]

# PostgreSQL (production)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db_name",
        "USER": "db_user",
        "PASSWORD": "db_pass",
        "HOST": "db_host",
        "PORT": "5432",
    }
}

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True