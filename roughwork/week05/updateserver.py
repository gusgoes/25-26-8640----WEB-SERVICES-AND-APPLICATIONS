import requests

book = {
    "title": "Jesus is amazing book",
    "author": "Gustavo",
    "price": 1000000
}

response = requests.post("http://127.0.0.1:5000/books", json=book, timeout=5)
print(response.status_code, response.json())