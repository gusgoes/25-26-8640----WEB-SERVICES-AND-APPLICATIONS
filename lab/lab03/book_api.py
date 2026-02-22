from api_functions import createbook, readbook, updatebook, deletebook

print("Starting...")
try:
    updatedbook = {"author": "Gus","id": 1686,"price": 15, "title": "Gustest Updated"}
    data = updatebook(1686, updatedbook)
    print("Success! Got:", data)

except Exception as e:
    print("Error:", e)

