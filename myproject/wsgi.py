"""WSGI config.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from . import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings.__name__)

application = get_wsgi_application()
