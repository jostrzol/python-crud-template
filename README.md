# Python CRUD template

A simple CRUD template based on FastAPI and SQLAlchemy.

# Configuration

Create a `.env` file:

```sh
DATABASE__URL = "postgresql://postgres@localhost/notes"
```

# Usage

To start the server run

```sh
uvicorn src.main.main:app --reload
```
