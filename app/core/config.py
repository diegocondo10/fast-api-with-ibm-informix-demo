import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTOR: str = 'http://host.docker.internal:5690/api/db'
    DEBUG: bool = False


settings = Settings()
