from flask import Flask, request

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_endpoint():
    return 'GET endpoint called HIHI'

@app.route('/post', methods=['POST'])
def post_endpoint():
    data = request.get_json()
    return f"POST endpoint called with data: {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
