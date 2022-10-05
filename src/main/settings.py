from pydantic import BaseSettings, BaseModel, PostgresDsn


class DatabaseSettings(BaseModel):
    url: PostgresDsn
    echo: bool = False
    wipe: bool = False


class Settings(BaseSettings):
    database: DatabaseSettings

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"
