from flask import Flask, request, jsonify
import requests
from flask import Blueprint

app7 = Blueprint('app7', __name__)


@app7.route('/')
def home():
    return 'Hello your In LAB API7:2023 Server Side Request Forgery'
    
@app7.route('/fetch_url', methods=['POST'])
def fetch_url():
    data = request.get_json()
    url = data.get('url')

    # Vulnerability: No proper URL validation and security checks
    response = requests.get(url)
    content = response.text

    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(debug=True)
