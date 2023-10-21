from flask import Flask, request, jsonify
from flask import Blueprint

app9 = Blueprint('app9', __name__)

# Initialize a global list to represent the inventory (for demonstration purposes)
inventory = []

@app9.route('/')
def home():
    return 'Hello your In LAB API9:2023 Improper Inventory Management'

# API endpoint to add an item to the inventory
@app9.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    item_name = data.get('item_name')
    item_quantity = data.get('item_quantity')

    if item_name and item_quantity:
        item = {
            'item_name': item_name,
            'item_quantity': item_quantity
        }
        inventory.append(item)
        return jsonify({"message": "Item added to inventory."}), 200
    else:
        return jsonify({"error": "Invalid data format."}), 400

# API endpoint to get the current inventory (improperly returns the raw global inventory list)
@app9.route('/get_inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

if __name__ == '__main__':
    app.run(debug=True)
