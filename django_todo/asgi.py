"""
ASGI config for django_todo project.

asgi.py contains the code that allows our web server
to communicate with our Python application.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')

application = get_asgi_application()
