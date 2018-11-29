from app import app

# from flask import Flask, Response, request, jsonify
# from flask_restful import Api

# import os

# app = Flask(__name__)
# app.secret_key = os.urandom(24)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5060, debug=True)
