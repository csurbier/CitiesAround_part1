"""
Django settings for  project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from prod_settings import *
#from dev_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '37o4*&^5)ic-8s!)&)+rf-klsnjvv%9h@m=hz@jid=s7*t*8r73'

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'bo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'citiesaround.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'citiesaround.wsgi.application'

#statics

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', ##''django.db.backends.postgresql_psycopg2',  #'django.db.backends.mysql',
        'DBNAME': POSTGRESQL_ADDON_DB,
        'NAME': POSTGRESQL_ADDON_DB,
        'USER': POSTGRESQL_ADDON_USER,
        'PASSWORD': POSTGRESQL_ADDON_PASSWORD,
        'HOST': POSTGRESQL_ADDON_HOST,
        'PORT': POSTGRESQL_ADDON_PORT,
        'URI' : POSTGRESQL_ADDON_URI,
    }
}

#Logging
U_LOGFILE_SIZE = 10 * 1024 * 1024
U_LOGFILE_COUNT = 2
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(MEDIA_ROOT, 'error.log'),
            'maxBytes': U_LOGFILE_SIZE,
            'backupCount': U_LOGFILE_COUNT,
            'formatter': 'verbose'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'bo': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
