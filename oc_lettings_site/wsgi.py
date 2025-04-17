"""
oc_lettings_site.wsgi
Point d’entrée WSGI pour déployer le projet sur un serveur compatible WSGI.

La variable ``application`` est détectée par des serveurs comme Gunicorn,
uWSGI ou mod_wsgi pour lancer Django en production.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# Objet WSGI attendu par le serveur HTTP
application = get_wsgi_application()
