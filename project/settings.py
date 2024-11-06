"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-32-w9phd*pzbgvvem943767ax3rh&odlq+q$69$qbb8p3=3m96'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp.apps.WebappConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql_psycopg2',
#          'NAME': 'postgres',
#          'HOST' : "db.fmlguqqzwmsqgobmvzll.supabase.co",
#          "PORT" : "5432",
#          'USER' : "postgres",
#          'PASSWORD' : "b7L4Ci3C45gwQpdp",
#      }
# }

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'postgres',
         'HOST' : "aws-0-eu-central-1.pooler.supabase.com",
         "PORT" : "6543",
         'USER' : "postgres.pjwjmibolcinplgzkfeo",
         'PASSWORD' : "coursetitans2024@#",
     }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


SUPABASE_URL = 'https://fmlguqqzwmsqgobmvzll.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZtbGd1cXF6d21zcWdvYm12emxsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MTgxMzEzMywiZXhwIjoxOTk3Mzg5MTMzfQ.SosGz7OXEzSeTkXCvFduDY59WxQ4xatl3ogDey7TDDM'
SUPABASE_BUCKET = 'Jetro'


# Base URL for accessing Supabase assets
SUPABASE_BUCKET_URL = 'https://fmlguqqzwmsqgobmvzll.supabase.co/storage/v1/object/public/Jetro/'


# Static files settings
STATIC_URL = "https://fmlguqqzwmsqgobmvzll.supabase.co/storage/v1/object/public/Jetro/static/"  # Assumes assets are stored in a directory named 'assets' in the bucket



# Media files settings
MEDIA_URL = f"{SUPABASE_BUCKET_URL}/media/"  # Assumes media files are stored in a 'media' folder in the bucket

# Remove STATICFILES_STORAGE backend since we're directly linking to Supabase

# Ensure these are either set correctly or removed if using a direct URL


# Primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication redirects
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = '/login/'
