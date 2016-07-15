"""
Django settings for  project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os

POSTGRESQL_ADDON_URI = os.getenv("POSTGRESQL_ADDON_URI")
POSTGRESQL_ADDON_PORT = os.getenv("POSTGRESQL_ADDON_PORT ")
POSTGRESQL_ADDON_HOST = os.getenv("POSTGRESQL_ADDON_HOST")
POSTGRESQL_ADDON_DB = os.getenv("POSTGRESQL_ADDON_DB")
POSTGRESQL_ADDON_PASSWORD = os.getenv("POSTGRESQL_ADDON_PASSWORD")
POSTGRESQL_ADDON_USER = os.getenv("POSTGRESQL_ADDON_USER")

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

MEDIA_URL = 'storage/'
MEDIA_ROOT = '/home/bas/app_76b49ba4-9531-497c-a210-b553dd7ec172/static/storage/'
STATIC_ROOT = '/home/bas/app_76b49ba4-9531-497c-a210-b553dd7ec172/static/static/'


# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# To send push on production set Debug=FALSE sinon a TRUE en PREPROD
DEBUG = False

