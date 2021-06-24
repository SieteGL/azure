"""
ASGI config for LindaSonrisa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
#We add the .local to do a direct execution 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LindaSonrisa.settings.local')

application = get_asgi_application()
