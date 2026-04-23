import requests

urlbook = "http://andrewbeatty1.pythonanywhere.com/books"

def readbook(book_id=None):
    if book_id is None:
        response = requests.get(urlbook)
    else:
        geturl = urlbook + "/" + str(book_id)
        response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(urlbook, json=book)
    return response.json()

def updatebook(book_id, book):
    puturl = urlbook + "/" + str(book_id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(book_id):
    deleteurl = urlbook + "/" + str(book_id)
    response = requests.delete(deleteurl)
    return response.json()