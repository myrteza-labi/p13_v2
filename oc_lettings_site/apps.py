"""
oc_lettings_site.apps
Déclare la configuration principale du projet Django **oc_lettings_site**.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Configuration d’application pour le projet racine *OC Lettings Site*.

    Cette classe est référencée dans ``INSTALLED_APPS`` sous
    ``'oc_lettings_site.apps.OCLettingsSiteConfig'``.
    """
    name = "oc_lettings_site"
