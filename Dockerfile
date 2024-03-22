FROM python:3.9

# Installation du package MySQL Connector Python
RUN pip install mysql-connector-python

# Installation de Flask
RUN pip install flask

# Copie de l'application Python dans le conteneur
COPY app.py /app/

# Définition du répertoire de travail
WORKDIR /app

# Exposition du port 5000
EXPOSE 5000

# Commande par défaut pour exécuter l'application
CMD ["python", "app.py"]

