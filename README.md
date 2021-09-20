# Building APIs with Django and Django Rest Framework for Tracking products

Develop an API that allows you to view products in the store, make purchases, and
add products.

## Requirements

Python 3.6\
Django 3.1\
Django REST Framework\
drf-yasg\
psycopg2-binary


## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

```bash
python -m venv env
```
After this, it is necessary to activate the virtual environment\
You can install all the required dependencies by running

```bash
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources.\

| Endpoint      | HTTP Method   | Result                    |
| ------------- |:-------------:| -----:                    |
| /api/stores/  | GET           |  Returns a list of stores |
| /api/stores/<store_id>/       | GET      |   Returns information about a specific store |
| /api/products/  | GET           |  Returns a list of products |
| /api/products/<products_id>/       | GET      |   Returns information about a specific products |
| /api/stores/<store_id>/buy/    | POST      |  Endpoint for purchasing products in the store. |
| /api/v1/stores/<store_id>/add/ | POST | Endpoint for adding a product to the store.

Also for better virtualization  of our APIs, drf-yasg has been chosen which Generate **real** Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.
**Using**
```bash
http://127.0.0.1:8000/swagger/
```


