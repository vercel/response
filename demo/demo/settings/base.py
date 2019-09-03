"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import logging
from response.slack.client import SlackClient
from pdpyras import APISession



from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5m*pc(gb!k+!913@qh2u5z7^s-bbp2ytw28gdvcbly5ayw1i5+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'after_response',
    'rest_framework',
    'bootstrap4',
    'social_django',
    'response.apps.ResponseConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = {
    # 'django.contrib.auth.backends.ModelBackend', # To keep the Browsable API
    'social_core.backends.github.GithubOrganizationOAuth2',
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'


# Django Rest Framework
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

# Markdown Filter

MARKDOWN_FILTER_WHITELIST_TAGS = [
    'a',
    'p',
    'code',
    'h1',
    'h2',
    'ul',
    'li',
    'strong',
    'em',
    'img',
]

MARKDOWN_FILTER_WHITELIST_ATTRIBUTES = [
    'src',
    'style',
]

MARKDOWN_FILTER_WHITELIST_STYLES = [
    'width', 'height', 'border-color', 'background-color',
    'white-space', 'vertical-align', 'text-align',
    'border-style', 'border-width', 'float', 'margin',
    'margin-bottom', 'margin-left', 'margin-right', 'margin-top'
]

def get_env_var(setting, warn_only=False):
    value = os.getenv(setting, None)

    if not value:
        error_msg = f"ImproperlyConfigured: Set {setting} environment variable"
        if warn_only:
            logger.warn(error_msg)
        else:
            raise ImproperlyConfigured(error_msg)
    else:
        value = value.replace('"', '')  # remove start/end quotes

    return value

SLACK_TOKEN = get_env_var("SLACK_TOKEN")
SLACK_CLIENT = SlackClient(SLACK_TOKEN)

PAGER_DUTY_TOKEN = get_env_var("PAGER_DUTY_TOKEN")
PAGER_DUTY_BASE_URL = get_env_var("PAGER_DUTY_BASE_URL")
PDSESSION = APISession(PAGER_DUTY_TOKEN)

