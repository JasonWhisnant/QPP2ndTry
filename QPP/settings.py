"""
Django settings for QPP project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u&)3i60w4nabvbmgfp)ecm+w$3_8n9p3c=#*855i!xbz^s=2nk'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = False
# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'EmpReview.apps.EmpreviewConfig',
    # 'okta_oauth2.apps.OktaOauth2Config',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add whitenoise middleware after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'okta_oauth2.middleware.OktaMiddleware',
]

ROOT_URLCONF = 'QPP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('EmpReview/templates')],
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

WSGI_APPLICATION = 'QPP.wsgi.application'

# Authentication Backend
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/

"""
AUTHENTICATION_BACKENDS = ("okta_oauth2.backend.OktaBackend")

OKTA_AUTH = {
    "ORG_URL": "https://eso.okta.com/",
    "ISSUER": "https://eso.okta.com/oauth2/default",
    "CLIENT_ID": "0oa40pfk2f8RksO7R697",
    "CLIENT_SECRET": "zcbQa6lf8EisG_sKDILsWOzEayA4c9FNfgWi1kpZ",
    "SCOPES": "openid profile email offline_access groups",
    "REDIRECT_URI": "http://localhost:8000/accounts/oauth2/callback",
    "LOGIN_REDIRECT_URL": "/",
    "CACHE_PREFIX": "okta",
    "CACHE_ALIAS": "default",
    "PUBLIC_NAMED_URLS": (),
    "USE_USERNAME": False,
    "MANAGE_GROUPS": False,
    "SUPERUSER_GROUP": "QPP Admins",
    "STAFF_GROUP": "QPP Approvers",
}
"""

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
# print("Pulled STATIC_URL from Settings")
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# print("Pulled STATICFILES_STORAGE from Settings")
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# print("Pulled STATIC_ROOT from Settings.")
print("SETTINGS:\nStaticFiles Dirs: None", "\nStatic URL: ", STATIC_URL, "\nStaticFiles Storage: ", STATICFILES_STORAGE, "\nStatic Root: ", STATIC_ROOT)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
 #