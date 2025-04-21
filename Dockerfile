# Image légère de Python
FROM python:3.10-slim

# Empêche les messages Python .pyc / stdout buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crée un dossier de travail
WORKDIR /app

# Installe les dépendances système utiles
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Copie les dépendances Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code
COPY . .

# Collecte les fichiers statiques (optionnel mais recommandé si tu utilises whitenoise)
RUN python manage.py collectstatic --noinput

# Expose le port utilisé par Gunicorn
EXPOSE 8000

# Commande de démarrage avec Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
