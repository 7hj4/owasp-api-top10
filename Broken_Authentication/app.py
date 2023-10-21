from flask import Flask, request, jsonify
from flask import Blueprint

app2 = Blueprint('app2', __name__)

# Dummy data representing user accounts
users = [
    {"id": 1, "username": "admin", "password": "admin123"},
    {"id": 2, "username": "user1", "password": "password1"},
    {"id": 3, "username": "user2", "password": "password2"},
]

@app2.route('/')
def home():
    return('Hello your In LAB API2:2023 Broken Authentication') 

# Function to authenticate a user
def authenticate(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

# API endpoint for user login (vulnerable to Broken Authentication)
@app2.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # In this vulnerable code, there are no proper authentication checks.
    # Any username and password combination is accepted.
    
    user = authenticate(username, password)
    if user:
        return jsonify({"message": "Login successful", "user_id": user["id"]})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

