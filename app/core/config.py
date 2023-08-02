import pathlib

from pydantic_settings import BaseSettings 

ROOT = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "SECRET_KEY"
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"

    class Config:
        case_sensitive = True

settings = Settings()

