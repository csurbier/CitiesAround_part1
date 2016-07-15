# *coding: utf-8*
import sys
import os
sys.path.append("/home/bas/app_76b49ba4-9531-497c-a210-b553dd7ec172")
os.environ['DJANGO_SETTINGS_MODULE'] = 'citiesaround.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-egg'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
