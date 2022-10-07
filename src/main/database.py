from contextlib import contextmanager
import logging
from typing import Callable, Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from .models import Base


logger = logging.getLogger(__name__)
logging.getLogger('sqlalchemy').setLevel(logging.INFO)


class Database:

    def __init__(self, url: str, echo: bool) -> None:
        self._engine = create_engine(
            url=url,
            echo=echo,
        )
        self._session_factory: Callable[..., Session] = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                future=True,
                bind=self._engine,
            )
        )

    def create_database(self, wipe: bool = False) -> None:
        if wipe:
            Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Iterator[Session]:
        session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.error("Session exception. Rolling back.")
            session.rollback()
            raise
        finally:
            session.close()
