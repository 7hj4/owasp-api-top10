from flask import Flask, request, jsonify
from flask import Blueprint

app3 = Blueprint('app3', __name__)

@app3.route('/')
def home():
    return 'Hello your In LAB API3:2023 Broken Object Property Level Authorization'
    
    
# Dummy data representing user accounts
users = [
    {"id": 1, "username": "yousef", "role": "admin"},
    {"id": 2, "username": "user1", "role": "user"},
    {"id": 3, "username": "user2", "role": "user"},
]

# Dummy data representing objects with properties and ownership
objects = [
    {"id": 1, "name": "Object 1", "owner_id": 1, "is_admin": True},
    {"id": 2, "name": "Object 2", "owner_id": 2, "is_admin": False},
]

# Function to find a user by ID
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

# API endpoint to update an object's properties (vulnerable to BOPA)
@app3.route('/objects/<int:object_id>', methods=['PUT'])
def update_object_properties(object_id):
    data = request.get_json()
    
    # Find the object by ID
    obj = get_object_by_id(object_id)
    
    # Check if the object exists
    if obj is None:
        return jsonify({"error": "Object not found"}), 404
    
    # Find the user making the request
    user_id = 1  # You should replace this with the actual user ID from authentication
    user = get_user_by_id(user_id)
    
    # Check if the user exists
    if user is None:
        return jsonify({"error": "User not found"}), 404
    
    # Check if the user is the owner or has admin privileges
    if user["role"] == "admin" or user["id"] == obj["owner_id"]:
        # In this vulnerable code, we allow anyone to update the "is_admin" property of an object.
        obj["is_admin"] = data.get("is_admin", obj["is_admin"])
        return jsonify({"message": "Object properties updated successfully","is_admin":obj["is_admin"],"username":user["username"],})
    else:
        return jsonify({"error": "Unauthorized: You don't have permission to update object properties"}), 403

if __name__ == '__main__':
    app.run(debug=True)
