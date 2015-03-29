"""
Django settings for django_tutorial_blog_ng project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8!43u8$-w9f%183r7ib)%ncuj!dyle0@&kj&w8hjq(d96b=!2t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.syndication',
    'django.contrib.sitemaps',
    'easy_maps',
    'blogengine',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'webchallenge_task.urls'

WSGI_APPLICATION = 'webchallenge_task.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'blogengine/../templates')]

STATIC_URL = '/static/'

LOGIN_URL = '/login/'

import dj_database_url
DATABASES['default'] =  dj_database_url.config(default="sqlite:///db.sqlite3")

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'volunteers.mail.robot@gmail.com'
EMAIL_HOST_PASSWORD = 'rdt123RDT'