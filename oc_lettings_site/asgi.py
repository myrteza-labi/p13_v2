"""
oc_lettings_site.asgi
Point d’entrée ASGI pour déployer le projet sur un serveur asynchrone.

Ce module expose la variable ``application`` que les serveurs compatibles ASGI
(Uvicorn, Daphne, Hypercorn…) utiliseront pour lancer Django.
"""

import os
from django.core.asgi import get_asgi_application

# Définit le module de configuration Django par défaut
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# Objet ASGI attendu par l’hébergeur (équivalent à wsgi.application)
application = get_asgi_application()
