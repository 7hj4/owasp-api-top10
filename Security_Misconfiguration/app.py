from flask import Flask, jsonify
from flask import Blueprint

app8 = Blueprint('app8', __name__)

@app8.route('/')
def home():
    return 'Hello your In LAB API8:2023 Security Misconfiguration'
    # Simulated security misconfiguration: Debug mode is enabled
    app.debug = True
    return jsonify({'message': 'Welcome to the home page!'})

if __name__ == '__main__':
    app.run()
