from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.main.models.base import Base
from src.main.settings import Settings

engine = create_engine(Settings().database.connection_string)

Base.metadata.create_all(engine)
