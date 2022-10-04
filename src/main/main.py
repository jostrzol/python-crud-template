from fastapi import FastAPI, status

from src.main.database.database import engine


app = FastAPI()


@app.post("/notes", status_code=status.HTTP_201_CREATED)
def post_note():
    return {"todo": "create a note"}


@app.get("/notes/{id}")
def get_note(id: int):
    return {"todo": "return a note"}


@app.put("/notes/{id}")
def put_note(id: int):
    return {"todo": "update a note"}


@app.delete("/notes/{id}")
def delete_note(id: int):
    return {"todo": "delete a note"}


@app.get("/notes")
def get_notes():
    return {"todo": "return all notes"}
