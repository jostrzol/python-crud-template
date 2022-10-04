from sqlalchemy import Column, VARCHAR, INTEGER, TEXT

from .base import Base


class Note(Base):
    __tablename__ = "notes"
    id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR(64))
    content = Column(TEXT)
