"""
profiles.views
Vues HTTP pour l’application **profiles**.

Contient :
- `profiles_index` : liste tous les profils.
- `profile` : affiche le détail d’un profil utilisateur.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile

# --------------------------------------------------------------------------- #
# Vues principales
# --------------------------------------------------------------------------- #


def profiles_index(request):
    """
    Page listant l’ensemble des profils.

    Parameters
    ----------
    request : HttpRequest
        Requête HTTP entrante.

    Returns
    -------
    HttpResponse
        Rendu du template ``profiles/index.html`` avec le contexte :
        ``{'profiles_list': <QuerySet[Profile]>}``.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Page de détail pour un utilisateur donné.

    Parameters
    ----------
    request : HttpRequest
        Requête HTTP entrante.
    username : str
        Nom d’utilisateur dont on souhaite afficher le profil.

    Returns
    -------
    HttpResponse
        Rendu du template ``profiles/profile.html`` avec le contexte :
        ``{'profile': <Profile>}``.
    """
    profile_obj = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile_obj}
    return render(request, "profiles/profile.html", context)
