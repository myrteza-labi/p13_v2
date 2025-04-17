"""
profiles.apps
Déclare la configuration Django de l’application **profiles**.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration d’application pour **profiles**.

    Cette classe est détectée automatiquement par Django et permet
    d’enregistrer l’app dans INSTALLED_APPS via
    ``'profiles.apps.ProfilesConfig'``.
    """
    name = "profiles"
