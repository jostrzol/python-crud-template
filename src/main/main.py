from fastapi import FastAPI, status
from sqlalchemy.orm import Session

from src.main.database.database import engine
from src.main import models
from src.main import schemas


app = FastAPI()


@app.post("/notes", status_code=status.HTTP_201_CREATED,
          response_model=schemas.Note)
def create_note(request: schemas.CreateNote):
    with Session(engine) as session:
        note = request.to_model()
        session.add(note)
        session.commit()
        result = schemas.Note(
            id=note.id,
            title=note.title,
            content=note.content
        )

    return result


@app.get("/notes/{id}")
def read_note(id: int):
    return {"todo": "return a note"}


@app.put("/notes/{id}")
def update_note(id: int):
    return {"todo": "update a note"}


@app.delete("/notes/{id}")
def delete_note(id: int):
    return {"todo": "delete a note"}


@app.get("/notes")
def read_all_notes():
    return {"todo": "return all notes"}
