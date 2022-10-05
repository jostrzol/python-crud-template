from typing import List

from fastapi import APIRouter, Depends, status, Response
from dependency_injector.wiring import inject, Provide

from .schemas import NoteResponse, NoteRequest, MessageResponse, error_message_response
from .containers import Container
from .services import NoteService
from .repositories import NoteNotFoundError, DuplicateTitleError


router = APIRouter()

BAD_NOTE_REQUEST_ERROR_RESP = {
        400: {
            "description": "Bad note request",
            "model": MessageResponse
        }
}

NOTE_NOT_FOUND_ERROR_RESP = {
        404: {
            "description": "Note note found",
            "model": MessageResponse
        }
}


@router.post(
    "/notes",
    status_code=status.HTTP_201_CREATED,
    response_model=NoteResponse,
    responses=BAD_NOTE_REQUEST_ERROR_RESP
)
@inject
def create_note(
    request: NoteRequest,
    note_service: NoteService = Depends(Provide[Container.note_service])
):
    try:
        return note_service.create_note(request)
    except DuplicateTitleError as e:
        return error_message_response(e, status.HTTP_400_BAD_REQUEST)


@router.get(
    "/notes/{note_id}",
    response_model=NoteResponse,
    responses=NOTE_NOT_FOUND_ERROR_RESP
)
@inject
def read_note(
    note_id: int,
    note_service: NoteService = Depends(Provide[Container.note_service])
):
    try:
        return note_service.get_note_by_id(note_id)
    except NoteNotFoundError as e:
        return error_message_response(e, status.HTTP_404_NOT_FOUND)


@router.put(
    "/notes/{note_id}",
    response_model=NoteResponse,
    responses=NOTE_NOT_FOUND_ERROR_RESP | BAD_NOTE_REQUEST_ERROR_RESP
)
@inject
def update_note(
    note_id: int,
    request: NoteRequest,
    note_service: NoteService = Depends(Provide[Container.note_service])
):
    try:
        return note_service.update_note(note_id=note_id, request=request)
    except NoteNotFoundError as e:
        return error_message_response(e, status.HTTP_404_NOT_FOUND)
    except DuplicateTitleError as e:
        return error_message_response(e, status.HTTP_400_BAD_REQUEST)


@router.delete(
    "/notes/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses=NOTE_NOT_FOUND_ERROR_RESP
)
@inject
def delete_note(
    note_id: int,
    note_service: NoteService = Depends(Provide[Container.note_service])
):
    try:
        note_service.delete_note_by_id(note_id)
    except NoteNotFoundError as e:
        return error_message_response(e, status.HTTP_404_NOT_FOUND)


@router.get("/notes", response_model=List[NoteResponse])
@inject
def read_all_notes(
    note_service: NoteService = Depends(Provide[Container.note_service])
):
    return note_service.get_all_notes()
