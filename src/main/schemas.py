from fastapi.responses import JSONResponse
from pydantic import BaseModel, NonNegativeInt


class NoteRequest(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    note_id: NonNegativeInt
    title: str
    content: str


class MessageResponse(BaseModel):
    message: str


def error_message_response(
    exception: Exception,
    status: int,
):
    content = MessageResponse(message=str(exception)).dict()
    return JSONResponse(
        status_code=status,
        content=content,
    )
