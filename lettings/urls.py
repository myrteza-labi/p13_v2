"""
lettings.urls
Table de routage URL pour l’application **lettings**.

Toutes les URLs de cette app sont préfixées dans le projet principal par
« /lettings/ » (via `include('lettings.urls', namespace='lettings')`).
"""

from django.urls import path
from . import views

app_name = "lettings"

urlpatterns = [
    # /lettings/
    path("", views.lettings_index, name="index"),
    # /lettings/3/
    path("<int:letting_id>/", views.letting, name="letting"),
]
