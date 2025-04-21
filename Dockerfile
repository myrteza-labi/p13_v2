# Image légère de Python
FROM python:3.10-slim

# Empêche les fichiers .pyc et force le log immédiat
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail
WORKDIR /app

# Installe les dépendances système
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Installe les dépendances Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie le projet dans l'image
COPY . .

# Expose le port utilisé
EXPOSE 8000

# Commande de démarrage : migrate + collectstatic + Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]
