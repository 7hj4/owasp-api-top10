from flask import Flask, jsonify
from flask import Blueprint

app10 = Blueprint('app10', __name__)

@app10.route('/')
def home():
    return 'Hello your In LAB API10:2023 Unsafe Consumption of APIs'

@app10.route('/data/<user_input>' ,methods=['GET'])
def unsafe_api_call(user_input):
    # Construct an API query without proper input validation (unsafe consumption)
    api_url = f"https://example.com/api/data?input={user_input}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return "Error: Unable to fetch data from the API"

if __name__ == "__main__":
    #user_input = input("Enter a value: ")
    #result = unsafe_api_call(user_input)
    print(result)
