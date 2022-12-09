"""
Django settings for purple_pages project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import logging
import ldap
import os
from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType
from pathlib import Path
from decouple import config
from dj_database_url import parse as db_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# Get DEBUG setting from setting.ini
##### SECURITY WARNING: don't run with debug turned on in production! #####
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

# Get allowed hosts from settings.ini
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [
#                        s.strip() for s in v.split(',')])

# Application definition

INSTALLED_APPS = [
    # Default Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',

    # Added functionality Apps
    'rest_framework',
    'rest_framework_datatables',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_bootstrap5',
    'imagekit',

    # Project Apps
    # 'pages',
    'persons',
    'dining',
    'api.apps.ApiConfig',
    # 'templates.media',

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

ROOT_URLCONF = 'one_stop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, "templates")],
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]


WSGI_APPLICATION = 'purple_pages.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': config(
        # JB: Connect to MySQL HPU server.
        'DATABASE_URL',
        cast=db_url
    ),
    'bbts': config(
        'BBTS_DATABASE_URL',
        cast=db_url
    ),
    # 'ccure': config(
    #     'CCURE_DATABASE_URL',
    #     cast=db_url
    # )

    'ccure': {
        'ENGINE': 'mssql',
        'NAME': 'ACVSCore',
        'HOST': config('CCURE_HOST'),
        'USER': config('CCURE_USER'),
        'PASSWORD': config('CCURE_PWD'),
        'PORT': '1433',
        'OPTIONS': {
            'dsn': 'vprodsec002',
            'driver': 'SQL Server Native Client 11.0',
        }
    },
    'kolkata': {
        'ENGINE': 'mssql',
        'NAME': 'idm_prod',
        'HOST': config('KOLKATA_HOST'),
        'USER': config('KOLKATA_USER'),
        'PASSWORD': config('KOLKATA_PWD'),
        'PORT': '1433',
        'OPTIONS': {
            'dsn': 'kolkata',
            'driver': 'SQL Server Native Client 11.0',
        }
    },

    'kolkata_ods': {
        'ENGINE': 'mssql',
        'NAME': 'ods_prod',
        'HOST': config('KOLKATA_HOST'),
        'USER': config('KOLKATA_USER'),
        'PASSWORD': config('KOLKATA_PWD'),
        'PORT': '1433',
        'OPTIONS': {
            'dsn': 'kolkata',
            'driver': 'SQL Server Native Client 11.0',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'persons/static/'),
    os.path.join(BASE_DIR, 'dining/static/'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

LOGIN_REDIRECT_URL = '/persons'

LOGOUT_REDIRECT_URL = '/login'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 50,
}


# We don't want persistent sessions
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


#####################################
######## LDAP Settings ##############
#####################################

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"django_auth_ldap": {"level": "DEBUG", "handlers": ["console"]}},
}

# Active Directory Auth Settings
AUTH_LDAP_SERVER_URI = config('AD_SERVER')
AUTH_LDAP_AD_BASE_DN = "dc=highpoint,dc=edu"
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True
AUTH_LDAP_BIND_DN = config('BIND_DN')
AUTH_LDAP_BIND_PASSWORD = config('AD_PWD')

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "OU=Active,OU=Campus,%s" % AUTH_LDAP_AD_BASE_DN, ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"
)

# AUTH_LDAP_GROUP_SEARCH is an LDAPSearch object that identifies the set of relevant group objects.
# That is, all groups that users might belong to as well as any others that we might need to know about
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "OU=Employees (Depts.),OU=campus,%s" % AUTH_LDAP_AD_BASE_DN, ldap.SCOPE_SUBTREE, "(objectClass=group)",
)

# AUTH_LDAP_GROUP_TYPE is an instance of the class corresponding to the type of group that will be returned by AUTH_LDAP_GROUP_SEARCH
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

# If AUTH_LDAP_REQUIRE_GROUP is set, then only users who are members of that group will successfully authenticate.
AUTH_LDAP_REQUIRE_GROUP = "CN=easgroup,OU=Groups,OU=Information Technology,OU=Employees (Depts.),OU=campus,%s" % AUTH_LDAP_AD_BASE_DN

# This is a dictionary that maps user model keys, respectively, to (case-insensitive) LDAP attribute names:
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "username": "name"
}

# A mapping from boolean User field names to distinguished names of LDAP groups.
# # The corresponding field is set to True or False according to whether the user is a member of the group.
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "CN=easgroup,OU=Groups,OU=Information Technology,OU=Employees (Depts.),OU=campus,%s" % AUTH_LDAP_AD_BASE_DN,
    "is_staff": "CN=easgroup,OU=Groups,OU=Information Technology,OU=Employees (Depts.),OU=campus,%s" % AUTH_LDAP_AD_BASE_DN,
    "is_superuser": "CN=easgroup,OU=Groups,OU=Information Technology,OU=Employees (Depts.),OU=campus,%s" % AUTH_LDAP_AD_BASE_DN
}

AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_AD_FIND_GROUP_PERMS = True
AUTH_LDAP_AD_GROUP_CACHE_TIMEOUT = 3600

# LDAPBackend runs first checking authentication with Active Directory
# ModelBackend runs second checking authentication with Django Database (MySQL server)
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)