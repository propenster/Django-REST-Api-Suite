# Django-REST-Api-Suite
A Minimalistic RESTful API Suite for ecommerce, health, economic, and other types of data built in Django using the Django Rest Framework.

### To Bootstrap
git clone this repo

navigate - cd into the cloned directory... where you have manage.py

python manage.py runserver

the API is served at http://localhost:8000/api

#### Authenticate with TOkens
HTTP POST - http://localhost:8000/api/suite/v1/auth/auth-token
  param -> username
  param -> password
  {
    "username": "user1",
    "password": "pass@123"
  }
  
  *ResponseContent {
    "token": "323af066f595d022a3598f741df90607a4fe5d99"
  }

#### HEADERS

"Authorization" : "Token {token}"

##### All products
http://localhost:8000/api/suite/v1/products

Single Product: @param 'id'
http://localhost:8000/api/suite/v1/products/15


##### All Books
http://localhost:8000/api/suite/v1/books

Single Book: @param 'id'
http://localhost:8000/api/suite/v1/book/5




