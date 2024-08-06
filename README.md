# REST API CRUD with Django

## Requirements
* Python3
* Pip v.24.1.2
* Pipenv
* Django v.5.0.7

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command
```
pipenv shell
pipenv install
```
## Use
First, add env for your database.
```
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=mysecretpassword
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```
Then, run the migrations with this command.
```
python manage.py migrate
```
In this project, we have several branch. You must checkout to one branch except master. For example, checkout to branch with-view-set.

After checkout, you can start the server, to start up Django's development server, run this command.
```
python manage.py runserver
```
In default, server port will be 8000. So, you can access:
* http://127.0.0.1:8000/api/products/ for list all products
* http://127.0.0.1:8000/api/products/<id product> for access the product detail
