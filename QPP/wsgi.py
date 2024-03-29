"""
WSGI config for QPP project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Check for the WEBSITE_HOSTNAME environment variable to see if we are running in Azure App Service
# If so, then load the settings from production.py
print('HERE IS THE VARIABLE!!!!!!!!:', os.environ['WEBSITE_HOSTNAME'])
settings_module = 'QPP.production' if 'WEBSITE_HOSTNAME' in os.environ else 'QPP.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
