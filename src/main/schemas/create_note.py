from pydantic import BaseModel

from src.main.models.note import Note


class CreateNote(BaseModel):
    title: str
    content: str

    def to_model(self) -> Note:
        return Note(
                title=self.title,
                content=self.content,
            )
