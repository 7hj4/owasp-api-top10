from flask import Flask, request, jsonify
import time
from flask import Blueprint

app4 = Blueprint('app4', __name__)

books = [

	# Dummy Data 
	
	{"id":1,"books":"book1"},
	{"id":2,"books":"book2"},
	{"id":3,"books":"book3"},
	{"id":4,"books":"book4"},

]


def get_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

@app4.route('/')
def home():
    return('Hello your In LAB API4:2023 Unrestricted Resource Consumption') 
    

@app4.route('/book/<int:book_id>', methods=['GET'])
def get_profile(book_id):
    #user_id = request.args.get('user_id')
    
    # Simulate a time-consuming operation
    #time.sleep(10)
    #user_id = 1
   
    book = get_book_by_id(book_id)
     
    if book is not None:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

