"""
Django settings for  project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Definition des variables d'environnement de CleverCloud
os.environ["POSTGRESQL_ADDON_URI"] = "postgis://user:password@bdsn15qbq8xaqoa-postgresql.services.clever-cloud.com:5432/bdsn15qbq8xaqoa"
os.environ["POSTGRESQL_ADDON_PORT"] = "5432"
os.environ["POSTGRESQL_ADDON_HOST"] = "bdsn15qbq8xaqoa-postgresql.services.clever-cloud.com"
os.environ["POSTGRESQL_ADDON_DB"] = "bdsn15qbq8xaqoa"
os.environ["POSTGRESQL_ADDON_PASSWORD"] = "password" # Votre mot de passe
os.environ["POSTGRESQL_ADDON_USER"] = "user" # Votre nom d'utilisateur
os.environ["APP_PATH"] = BASE_DIR
os.environ["VIRTUAL_HOST"] = "http://localhost:8000"
#Injection par CleverCloud
POSTGRESQL_ADDON_URI = os.getenv("POSTGRESQL_ADDON_URI")
POSTGRESQL_ADDON_PORT = os.getenv("POSTGRESQL_ADDON_PORT ")
POSTGRESQL_ADDON_HOST = os.getenv("POSTGRESQL_ADDON_HOST")
POSTGRESQL_ADDON_DB = os.getenv("POSTGRESQL_ADDON_DB")
POSTGRESQL_ADDON_PASSWORD = os.getenv("POSTGRESQL_ADDON_PASSWORD")
POSTGRESQL_ADDON_USER = os.getenv("POSTGRESQL_ADDON_USER")
MEDIA_URL = 'storage/'


MEDIA_ROOT = '/Users/csurbier/blog/citiesaround/citiesaround/static/storage/' 
STATIC_ROOT = '/Users/csurbier/blog/citiesaround/citiesaround/static/static/'
DEBUG = True
