from .schemas import NoteRequest, NoteResponse
from .models import Note


def note_model_to_response(model: Note) -> NoteResponse:
    return NoteResponse(
            note_id=model.note_id,
            title=model.title,
            content=model.content,
        )


def note_request_to_model(
        request: NoteRequest,
        note_id: int | None = None
) -> Note:
    return Note(
            note_id=note_id,
            title=request.title,
            content=request.content,
        )
