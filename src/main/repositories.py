from typing import Callable, List

from sqlalchemy import select
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

from .models import Note


class NoteRepository:

    def __init__(self, session_factory: Callable[..., Session]):
        self._session_factory = session_factory

    def save(self, note: Note):
        with self._new_session() as session:
            try:
                session.add(note)
                session.commit()
                session.refresh(note)
                return note
            except IntegrityError as e:
                raise DuplicateTitleError(note.title) from e

    def get_by_id(self, note_id: int) -> Note:
        with self._new_session() as session:
            statement = select(Note).filter_by(note_id=note_id)
            note: Note | None = session.execute(statement).scalars().first()
            if note is not None:
                print(note.note_id)
                return note
            else:
                raise NoteNotFoundError(note_id)

    def update(self, note: Note):
        with self._new_session() as session:
            try:
                session.merge(note)
                session.commit()
                return note
            except IntegrityError as e:
                raise DuplicateTitleError(note.title) from e

    def delete_by_id(self, note_id: int) -> None:
        with self._new_session() as session:
            statement = select(Note).filter_by(note_id=note_id)
            note: Note | None = session.execute(statement).scalars().first()
            if note is not None:
                session.delete(note)
                session.commit()
            else:
                raise NoteNotFoundError(note_id)

    def get_all(self) -> List[Note]:
        with self._new_session() as session:
            statement = select(Note)
            return session.execute(statement).scalars().all()

    def _new_session(self) -> Session:
        return self._session_factory()


class NoteNotFoundError(RuntimeError):
    def __init__(self, note_id: int):
        self.note_id = note_id
        super().__init__(f"note with id: {note_id} not found")

class DuplicateTitleError(RuntimeError):
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"note with title: '{title}' already defined")
