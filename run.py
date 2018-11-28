from flask import Flask, Response, request, jsonify

import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24) 

@app.route('/')
def index():
    return (jsonify({'notice' : 'Welcome to my API!'}))

@app.route('/red-flag')
def redFlag():
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5060,debug=True)