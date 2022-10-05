from sqlalchemy import Column, VARCHAR, INTEGER, TEXT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"
    note_id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR(64), unique=True)
    content = Column(TEXT)
