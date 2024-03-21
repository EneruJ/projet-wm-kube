import logging
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Configuration du niveau de journalisation et du format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

