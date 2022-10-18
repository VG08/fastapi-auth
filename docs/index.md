# fastapi-auth

This is a [FastAPI](https://fastapi.tiangolo.com) project to demonstrate how auth works in FastAPI with a fake db and
Docker.

The project can be run in either of the following ways:
```sh
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```

```sh
$ ./start-dev.sh
```

The `basic-example.py` file contains all the API routes and their basic logic along with the secrets and the fake
database.

The `crud.py` file contains methods to perform CRUD(Create-Read-Update-Delete) operations.

The `database.py` file contains the database engine, and also an instance of the db.

The `main.py` file contains several methods to authenticate and unauthenticate users and also perform some CRUD
operations, it also contains certain secrets, and crypographic variables and data.

The `models.py` file contians the data models for the database.

The `schemas.py` file contains the schema for FastAPI, as well as documentation.