"""
lettings.models
Définit les modèles de l’application **lettings** : Address et Letting.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse postale.

    Attributs
    ----------
    number : PositiveIntegerField
        Numéro de voie (max : 4 chiffres, valeur > 0).
    street : CharField
        Nom de la rue (longueur ≤ 64).
    city : CharField
        Ville (longueur ≤ 64).
    state : CharField
        Code d’état sur 2 lettres (par ex. : CA, NY), longueur fixe 2.
    zip_code : PositiveIntegerField
        Code postal américain (max : 5 chiffres, valeur > 0).
    country_iso_code : CharField
        Code ISO 3166‑1 alpha‑3 du pays (longueur fixe 3).

    Notes
    -----
    La pluralisation par défaut de Django sur « Address » donnait
    « Addresss ». Elle est corrigée via `verbose_name_plural = "Addresses"`.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Options de métadonnées pour Address."""
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self) -> str:
        """Retourne une représentation concise de l’adresse (numéro + rue)."""
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Modèle représentant une annonce de location.

    Attributs
    ----------
    title : CharField
        Titre de l’annonce (longueur ≤ 256).
    address : OneToOneField
        Référence unique vers un objet Address ; la suppression d’une adresse
        entraîne la suppression de la location associée (`on_delete=models.CASCADE`).
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """Options de métadonnées pour Letting."""
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"

    def __str__(self) -> str:
        """Retourne le titre complet de l’annonce."""
        return self.title
