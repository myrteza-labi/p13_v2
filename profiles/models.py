"""
profiles.models
Définit le modèle Profile pour l’application **profiles**.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extension du modèle ``User`` pour stocker une ville favorite.

    Attributs
    ---------
    user : OneToOneField
        L’utilisateur auquel le profil est associé.
        ``related_name='new_profile'`` permet d’accéder au profil depuis
        ``user.new_profile``.
    favorite_city : CharField
        Ville préférée de l’utilisateur (facultatif, longueur ≤ 64).
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="new_profile",
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self) -> str:
        """
        Retourne le nom d’utilisateur lié à ce profil.

        Returns
        -------
        str
            Nom d’utilisateur (``user.username``).
        """
        return self.user.username
