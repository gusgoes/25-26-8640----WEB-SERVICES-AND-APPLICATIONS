from flask import Flask, request, jsonify
from pathlib import Path
import json

app = Flask(__name__)

DATA_FILE = Path(__file__).with_name("books.json")
DEFAULT_BOOKS = [
    {"id": 1, "title": "Harry Goes Wild", "author": "J.K. Rowling", "price": 2999},
    {"id": 2, "title": "Python Basics", "author": "Guido van Rossum", "price": 3999}
]


def load_books():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    save_books(DEFAULT_BOOKS)
    return DEFAULT_BOOKS.copy()


def save_books(current_books):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(current_books, file, indent=2)


books = load_books()

@app.route('/')
def home():
    return "Welcome to the Book API! Try /books or /books/1"

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = None
    for b in books:
        if b['id'] == id:
            book = b
            break
        
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404
    
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    new_id = max([b['id'] for b in books], default=0) + 1
    new_book['id'] = new_id
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201

@app.route('/books/search', methods=['GET'])
def search_books():
    # Get query parameter from URL
    title_query = request.args.get('title', '')
    
    if not title_query:
        return jsonify({"error": "Please provide a title parameter"}), 400
    
    # Find matching books
    results = []
    for book in books:
        if title_query.lower() in book['title'].lower():
            results.append(book)
    
    return jsonify(results)

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    for i, b in enumerate(books):
        if b['id'] == id:
            deleted = books.pop(i)
            save_books(books)   
            return jsonify({"deleted": deleted}), 200
    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__": app.run(debug=True)