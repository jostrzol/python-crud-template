from pydantic import BaseSettings

from src.main.database.settings import DatabaseSettings


class Settings(BaseSettings):
    database: DatabaseSettings

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"

