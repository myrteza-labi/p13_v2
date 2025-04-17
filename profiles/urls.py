"""
profiles.urls
Table de routage URL pour l’application **profiles**.

Toutes les URLs de cette app sont préfixées dans le projet principal par
« /profiles/ » (via `include('profiles.urls', namespace='profiles')`).
"""

from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.profiles_index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
