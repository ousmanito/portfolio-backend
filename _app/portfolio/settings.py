"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


# Build paths inside the project like this: BASE_DIR / 'subdir'.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    default="@li16cr_r%h-lqe)w%5nkxxc!=*_v95#r5vqwfyy03+*%y4s3@",
)
# APPEND_SLASH = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "portfolio-backend-orcin.vercel.app",
    "portfolio-production-bde8.up.railway.app"
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", default=True)


CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
    "http://localhost:3100",
    "http://127.0.0.1:3100",
    "http://0.0.0.0:3100",
    "https://ousmanebathily.com",
    "https://portfolio-backend-orcin.vercel.app",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfolio",
    "rest_framework",
    "knox",
    "corsheaders",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": os.getenv("DJANGO_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DJANGO_DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
        "TEST": {
            "NAME": "DJANGO_TEST_DB",
        },
    }
}

if os.getenv("DOCKER_ENVIRONMENT") or os.getenv("PRODUCTION"):
    db = DATABASES["default"]
    db["USER"] = os.getenv("DJANGO_DB_USER")
    db["PASSWORD"] = os.getenv("DJANGO_DB_PASSWORD")
    db["HOST"] = os.getenv("DJANGO_DB_HOST")
    db["PORT"] = os.getenv("DJANGO_DB_PORT")


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")
STATIC_URL = "/static/"

AZURE_ACCOUNT_NAME = "datafactorydjangostorage"
AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")

if os.getenv("PRODUCTION"):
    MEDIA_URL = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/portfolio-media/"
else:
    MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "portfolio-media")

default_storage = {"default": {"BACKEND": "", "OPTIONS": {}}}


if os.getenv("PRODUCTION"):
    default_storage["default"][
        "BACKEND"
    ] = "storages.backends.azure_storage.AzureStorage"
    default_storage["default"]["OPTIONS"] = {
        "azure_container": "portfolio-media",
        "custom_domain": f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net",
        "account_key": AZURE_ACCOUNT_KEY,
        "account_name": AZURE_ACCOUNT_NAME,
    }
else:
    default_storage["default"][
        "BACKEND"
    ] = "django.core.files.storage.FileSystemStorage"


STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    }
}
STORAGES["default"] = default_storage["default"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Redis cache support
# https://docs.djangoproject.com/en/4.0/topics/cache/#redis-1

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": f"redis://{os.getenv('REDIS_HOST')}:6379/1",
#     }
# }
#
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Rest Framework

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "knox.auth.TokenAuthentication",
    ),
}
