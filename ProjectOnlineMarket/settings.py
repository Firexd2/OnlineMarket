"""
Django settings for ProjectOnlineMarket project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^15^e_=gzm!$#jhlhc(t4cyp#^ev^5_cr7+16g0xozbr2&s^=f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Core',
    'Baskets',
    'Orders',
    'Payment',
    'Products',
    'Authentication',
    'PersonalRoom',
    'widget_tweaks',
]

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Core.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Core.context_processors.get_info_for_all_page',
            ],
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

# Custom AdminPanel

ADMIN_TOOLS_INDEX_DASHBOARD = {
    'django.contrib.admin.site': 'Core.custom_admin.admin_dashboard.CustomIndexDashboard',
    'Core.admin.admin_panel': 'Core.custom_admin.min_admin_dashboard.CustomIndexDashboard',
}

ADMIN_TOOLS_MENU = {
    'django.contrib.admin.site': 'Core.custom_admin.admin_menu.CustomMenu',
    'Core.admin.admin_panel': 'Core.custom_admin.min_admin_menu.CustomMenu',
}


ADMIN_TOOLS_THEMING_CSS = '/static_for_admin/admin-theme.css'


# ADMIN_TOOLS_APP_INDEX_DASHBOARD = {
#     'django.contrib.admin.site': 'Core.custom_admin.admin_dashboard.CustomAppIndexDashboard',
#     'Core.admin.admin_panel': 'Core.custom_admin.min_admin_dashboard.CustomAppIndexDashboard',
# }


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'Core/static/',
]

WSGI_APPLICATION = 'ProjectOnlineMarket.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your Email'
EMAIL_HOST_PASSWORD = 'Email password'
EMAIL_PORT = 587

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/authentication/login/'

# Redis settings

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
