from pydantic import BaseModel, PostgresDsn


class DatabaseSettings(BaseModel):
    connection_string: PostgresDsn
