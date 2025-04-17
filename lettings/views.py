"""
lettings.views
Vues HTTP pour l’application **lettings**.

Contient :
- `lettings_index` : page listant toutes les annonces.
- `letting` : page de détail d’une annonce précise.
- `test_error` : déclenche volontairement une exception 500 pour tester la page d’erreur.
- `test_sentry` : déclenche une exception capturée par Sentry pour vérifier l’intégration.
"""

import logging
from django.shortcuts import render, get_object_or_404
from .models import Letting

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------- #
# Vues « utiles »
# --------------------------------------------------------------------------- #


def lettings_index(request):
    """
    Page d’accueil des lettings (liste des annonces).

    Parameters
    ----------
    request : HttpRequest
        Requête HTTP entrante.

    Returns
    -------
    HttpResponse
        Rendu du template ``lettings/index.html`` avec la liste des annonces.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Page de détail pour une annonce donnée.

    Parameters
    ----------
    request : HttpRequest
        Requête HTTP entrante.
    letting_id : int
        Identifiant primaire de l’annonce.

    Returns
    -------
    HttpResponse
        Rendu du template ``lettings/letting.html`` affichant le titre et l’adresse.
    """
    try:
        letting_obj = get_object_or_404(Letting, id=letting_id)
    except Exception as e:
        logger.error("Erreur lors de la récupération du letting %s : %s", letting_id, str(e))
        raise

    context = {
        "title": letting_obj.title,
        "address": letting_obj.address,
    }
    return render(request, "lettings/letting.html", context)


# --------------------------------------------------------------------------- #
# Vues de test (erreur 500 et Sentry)
# --------------------------------------------------------------------------- #


def test_error(request):
    """
    Déclenche une exception non gérée pour afficher la page 500 personnalisée.

    Parameters
    ----------
    request : HttpRequest
        Requête HTTP entrante.

    Raises
    ------
    Exception
        Toujours levée, contenant le message « Test d'erreur 500 ».
    """
    raise Exception("Test d'erreur 500")


def test_sentry(request):
    """
    Déclenche une exception capturée par Sentry pour valider l’intégration.

    Parameters
    ----------
    request : HttpRequest
        Requête HTTP entrante.

    Raises
    ------
    Exception
        Toujours levée, contenant le message « Test de Sentry ».
    """
    raise Exception("Test de Sentry")
