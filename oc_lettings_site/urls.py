"""
oc_lettings_site.urls
Table de routage URL du projet principal **OC Lettings Site**.

Inclut :
- Page d’accueil (``index``)
- Sous‑apps « lettings » et « profiles »
- Interface d’administration Django
- Routes de test pour la page 500 et l’intégration Sentry
"""

from django.contrib import admin
from django.urls import path, include

from lettings.views import test_error, test_sentry
from . import views

urlpatterns = [
    # Accueil du site : /
    path("", views.index, name="index"),
    # Sous‑app lettings : /lettings/
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    # Sous‑app profiles : /profiles/
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),
    # Admin Django : /admin/
    path("admin/", admin.site.urls),
    # Test page 500 : /test500/
    path("test500/", test_error, name="test_error"),
    # Test Sentry : /sentry-test/
    path("sentry-test/", test_sentry, name="sentry-test"),
]
