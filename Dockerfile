FROM python:3.9

# Installation du package MySQL Connector Python
RUN pip install mysql-connector-python

# Installation de Flask
RUN pip install flask

RUN pip install Flask-CORS

# Copie de l'application Python dans le conteneur
COPY app.py /app/

# Définition du répertoire de travail
WORKDIR /app

# Exposition du port 5000
EXPOSE 5000

# Définir la variable d'environnement MYSQL_HOST
ENV MYSQL_HOST=mysql-service-mezzache

# Commande par défaut pour exécuter l'application
CMD ["python", "app.py"]

