from sqlalchemy import Column, VARCHAR, INTEGER, TEXT

from .base import Base

class Note(Base):
    __tablename__ == "notes"
    id = Column(Integer(6), primary_key=True)
    title = Column(String(64))
    content = Column(TEXT)
