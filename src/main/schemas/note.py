from pydantic import BaseModel, NonNegativeInt


class Note(BaseModel):
    id: NonNegativeInt
    title: str
    content: str
