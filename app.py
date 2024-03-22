import logging
from flask import Flask, jsonify, request, render_template
import os
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration du niveau de journalisation et du format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Récupérer les informations de connexion à MySQL à partir des variables d'environnement
mysql_host = os.getenv("MYSQL_HOST", "10.0.36.81")
mysql_user = os.getenv("MYSQL_USER", "root")
mysql_password = os.getenv("MYSQL_PASSWORD", "password")
mysql_database = os.getenv("MYSQL_DATABASE", "mydatabase")

# Configuration de la connexion MySQL
db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    passwd=mysql_password,
    database=mysql_database
)

@app.route('/users')
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return jsonify({"users": users})
    
@app.route('/get', methods=['GET'])
def get_endpoint():
    ip = request.host.split(':')[0]
    app.logger.info('GET request received from IP: %s', ip)
    return jsonify({"message": "Hello World!", "server_ip": ip})

@app.route('/post', methods=['POST'])
def post_endpoint():
    data = request.get_json()
    app.logger.info('POST request received with data: %s', data)
    return f"POST endpoint called with data: {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

