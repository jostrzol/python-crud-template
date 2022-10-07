from sqlalchemy import Column, INTEGER, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"
    note_id: int = Column(INTEGER, primary_key=True)    # type: ignore
    title: str = Column(VARCHAR(64), unique=True)       # type: ignore
    content: str = Column(TEXT)                         # type: ignore
