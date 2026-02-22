import requests

urlgoogle = "https://google.com"
response = requests.get(urlgoogle)

print(response.text)
print(response.status_code)

urlbook = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(urlbook)
print(response.text)
print(response.json())

def readbook ():
    response = requests.get(urlbook)
    return response.json()
if __name__ == "__main__":
    print(readbook())

def readbook(id):
    geturl = urlbook + "/" + str(id)
    response = requests.get(geturl)
    return response.json()
if __name__ == "__main__":
    print(readbook(1680))

def createbook(book):
    response = requests.post(urlbook, json=book)
    return response.json()
if __name__ == "__main__":
    newbook = {"title": "Gustest", "author": "Gus", "price": 10.99}
    print(createbook(newbook))

def updatebook(id, book):
    puturl = urlbook + "/" + str(id)
    response = requests.put(puturl, json=book)
    print("PUT URL:", puturl)
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Raw body:", response.text[:300])

if __name__ == "__main__":
    updatedbook = {"author": "Gus","id": 1686,"price": 12, "title": "Gustest Updated"}
    print(updatebook(1686, updatedbook))

def deletebook(id):
    deleteurl = urlbook + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()
if __name__ == "__main__":
    print(deletebook(1686))