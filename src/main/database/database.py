from sqlalchemy import create_engine

from src.main.schema.base import Base
from src.main.settings import Settings

engine = create_engine(Settings().database.connection_string)

Base.metadata.create_all(engine)
