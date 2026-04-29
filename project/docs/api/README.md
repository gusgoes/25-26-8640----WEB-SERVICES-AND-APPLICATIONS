# Books API

Base URL (local):
http://127.0.0.1:5000

## Endpoints

### GET /books
Returns all books.

Response 200 example:
```json
[
	{
		"id": 1,
		"title": "1984",
		"author": "George Orwell",
		"price": 10.5
	}
]
```

### GET /books/{id}
Returns one book by id.

Response 200 example:
```json
{
	"id": 1,
	"title": "1984",
	"author": "George Orwell",
	"price": 10.5
}
```

Response 404 example:
```json
{
	"error": "Not found"
}
```

### POST /books
Creates a new book.

Request body example:
```json
{
	"title": "1984",
	"author": "George Orwell",
	"price": 10.5
}
```

Response 201 example:
```json
{
	"id": 1
}
```

Response 400 examples:
```json
{
	"error": "title is required and must be a non-empty string"
}
```

```json
{
	"error": "price must be greater than or equal to 0"
}
```

### PUT /books/{id}
Updates an existing book.

Request body example:
```json
{
	"title": "1984",
	"author": "George Orwell",
	"price": 8.99
}
```

Response 200 example:
```json
{
	"updated": 1
}
```

Response 400 example:
```json
{
	"error": "price is required and must be numeric"
}
```

Response 404 example:
```json
{
	"error": "Not found"
}
```

### DELETE /books/{id}
Deletes a book by id.

Response 200 example:
```json
{
	"deleted": 1
}
```

Response 404 example:
```json
{
	"error": "Not found"
}
```

## Validation Rules

For POST and PUT:
- title: required, string, not empty
- author: required, string, not empty
- price: required, numeric, must be greater than or equal to 0
