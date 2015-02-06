"""
WSGI config for web_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/dmitry/projects/Editable_table')
os.environ["DJANGO_SETTINGS_MODULE"] =  "web_app.settings"

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()