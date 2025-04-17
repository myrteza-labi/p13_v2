"""
oc_lettings_site.settings
Paramètres et configuration Django pour le projet *OC Lettings Site*.

Ce fichier regroupe :
- Configuration de Sentry.
- Réglages de base (BASE_DIR, DEBUG, ALLOWED_HOSTS…).
- Paramètres d’applications, middleware, base de données, i18n, statique, etc.
"""

from pathlib import Path
import os

from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# --------------------------------------------------------------------------- #
# Monitoring : configuration Sentry
# --------------------------------------------------------------------------- #

load_dotenv()  # Charge les variables définies dans .env

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),  # DSN cachée dans les variables d’env.
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,  # 100 % des performances capturées (à ajuster).
    send_default_pii=True,   # Envoie les infos d’utilisateur si dispo.
)

# --------------------------------------------------------------------------- #
# Chemins et clef secrète
# --------------------------------------------------------------------------- #

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

# --------------------------------------------------------------------------- #
# Exécution & hôtes
# --------------------------------------------------------------------------- #

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# --------------------------------------------------------------------------- #
# Applications installées
# --------------------------------------------------------------------------- #

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "lettings",
    "profiles",
]

# --------------------------------------------------------------------------- #
# Middleware
# --------------------------------------------------------------------------- #

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oc_lettings_site.urls"

# --------------------------------------------------------------------------- #
# Templates
# --------------------------------------------------------------------------- #

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "oc_lettings_site.wsgi.application"

# --------------------------------------------------------------------------- #
# Base de données
# --------------------------------------------------------------------------- #

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "oc-lettings-site.sqlite3"),
    }
}

# --------------------------------------------------------------------------- #
# Validation des mots de passe
# --------------------------------------------------------------------------- #

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------------------------------- #
# Internationalisation
# --------------------------------------------------------------------------- #

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --------------------------------------------------------------------------- #
# Fichiers statiques
# --------------------------------------------------------------------------- #

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
