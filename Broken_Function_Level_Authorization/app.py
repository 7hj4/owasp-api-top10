from flask import Flask, request, jsonify
from flask import Blueprint

app5 = Blueprint('app5', __name__)

# Simulated user data (for demonstration purposes only)
users = {
    'user1': {'role': 'user'},
    'user2': {'role': 'admin'},
}

@app5.route('/')
def home():
    return('Hello your In LAB API5:2023 Broken Function Level Authorization') 

@app5.route('/admin-panel', methods=['GET'])
def admin_panel():
    user = get_authenticated_user()

    # Vulnerability: No proper authorization check
    if user['role'] == 'admin':
        return jsonify({'Role':user['role'] ,'message': 'Welcome to the admin panel! You have full access.'})
    else:
        return jsonify({'message': 'Unauthorized access to the admin panel'}), 403

def get_authenticated_user():
    # Simulated authentication logic for demonstration purposes
    # In a real application, this would involve verifying user credentials, tokens, or session data
    authenticated_user = users.get(request.headers.get('Authorization'))
    if authenticated_user:
        return authenticated_user
    else:
        return {}


