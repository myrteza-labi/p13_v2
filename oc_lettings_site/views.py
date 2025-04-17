"""
oc_lettings_site.views
Vues globales du projet racine.

Pour le moment, seule la page d’accueil (`index`) est définie ici ;
les autres vues spécifiques se trouvent dans les applications
« lettings » et « profiles ».
"""

from django.shortcuts import render


def index(request):
    """
    Affiche la page d’accueil du site (template ``index.html``).

    Parameters
    ----------
    request : HttpRequest
        Requête HTTP entrante.

    Returns
    -------
    HttpResponse
        Rendu du template d’accueil.
    """
    return render(request, "index.html")
