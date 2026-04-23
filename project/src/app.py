import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from src.book_dao import book_dao

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(book_dao.get_all())

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = book_dao.find_by_id(id)
    if book is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(book)

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_id = book_dao.create(data)
    return jsonify({'id': new_id}), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    rows = book_dao.update(id, data)
    if rows == 0:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({'updated': id})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    rows = book_dao.delete(id)
    if rows == 0:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({'deleted': id})

if __name__ == "__main__":
    app.run(debug=True)