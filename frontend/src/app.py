from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def('http://backend-service/users')
    return jsonify(response.json())

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    response = requests.post('http://backend-service/users', json=user)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)