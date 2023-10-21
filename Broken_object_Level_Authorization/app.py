from flask import Flask, request, jsonify
from flask import Blueprint

app1 = Blueprint('app1', __name__)

# Dummy data representing user accounts
users = [
    {"id": 1, "username": "admin", "role": "admin"},
    {"id": 2, "username": "user1", "role": "user"},
    {"id": 3, "username": "user2", "role": "user"},
]

# Dummy data representing objects with different owners
objects = [
    {"id": 1, "name": "Object 1", "owner_id": 1},
    {"id": 2, "name": "Object 2", "owner_id": 2},
]

@app1.route('/')
def home():
    return 'Hello your In LAB API1:2023 Broken Object Level Authorization' 
    
# Function to find a user by ID
@app1.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Function to find an object by ID
def get_object_by_id(object_id):
    for obj in objects:
        if obj["id"] == object_id:
            return obj
    return None

# API endpoint to update an object's name (vulnerable to BOLA)
@app1.route('/objects/<int:object_id>', methods=['PUT'])
def update_object(object_id):
    data = request.get_json()
    new_name = data.get("new_name")

    # In this vulnerable code, there are no proper authorization checks.
    # Anyone can update any object's name, regardless of ownership.
    
    obj = get_object_by_id(object_id)
    if obj:
        obj["name"] = new_name
        return jsonify({"message": "Object name updated successfully"})
    else:
        return jsonify({"error": "Object not found"}), 404

    
    
