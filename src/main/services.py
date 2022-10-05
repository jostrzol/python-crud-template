from typing import List

from .schemas import NoteResponse, NoteRequest
from .repositories import NoteRepository
from .mappings import note_request_to_model, note_model_to_response


class NoteService:

    def __init__(self, note_repository: NoteRepository) -> None:
        self._repository = note_repository

    def create_note(self, request: NoteRequest) -> NoteResponse:
        note_model = note_request_to_model(request)
        self._repository.save(note_model)
        return note_model_to_response(note_model)

    def get_note_by_id(self, note_id: int) -> NoteResponse:
        note_model = self._repository.get_by_id(note_id)
        return note_model_to_response(note_model)

    def update_note(self, note_id: int,
                    request: NoteRequest) -> NoteResponse:
        note_model = note_request_to_model(request, note_id=note_id)
        self._repository.update(note_model)
        return note_model_to_response(note_model)

    def delete_note_by_id(self, note_id: int) -> None:
        self._repository.delete_by_id(note_id)

    def get_all_notes(self) -> List[NoteResponse]:
        return [
            note_model_to_response(note_model)
            for note_model in self._repository.get_all()
        ]
