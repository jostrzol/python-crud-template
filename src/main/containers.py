from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Factory, Singleton

from . import endpoints
from .database import Database
from .repositories import NoteRepository
from .services import NoteService
from .settings import Settings


class Container(DeclarativeContainer):

    wiring_config = WiringConfiguration(modules=[endpoints])

    config = Configuration(pydantic_settings=[Settings()])

    database = Singleton(
        Database,
        url=config.database.url,
        echo=config.database.echo
    )

    note_repository = Factory(
        NoteRepository,
        session_factory=database.provided.session,
    )

    note_service = Factory(
        NoteService,
        note_repository=note_repository,
    )
