# app.py
from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://backend-service:8080')

@app.route('/')
def index():
    response = requests.get(f'{BACKEND_URL}/api/users')
    users = response.json() if response.status_code == 200 else []
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = {
        'name': request.form.get('name'),
        'email': request.form.get('email')
    }
    requests.post(f'{BACKEND_URL}/api/users', json=user_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)