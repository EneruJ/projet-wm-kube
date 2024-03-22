import mysql.connector

# Informations de connexion à MySQL
mysql_host = "10.0.36.81"  # Remplacez par l'adresse du service MySQL
mysql_user = "root"  # Utilisateur MySQL
mysql_password = "password"  # Mot de passe MySQL

# Connexion à MySQL
db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    passwd=mysql_password
)

# Création de la base de données
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
cursor.execute("USE mydatabase")

# Création de la table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")

# Insertion de données dans la table
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
val = [
  ('John', 'john@example.com'),
  ('Emma', 'emma@example.com'),
  ('Michael', 'michael@example.com')
]
cursor.executemany(sql, val)

# Valider les changements et fermer la connexion
db.commit()
db.close()

print("Base de données, table et données ajoutées avec succès !")
