from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    ASYNC_DB_URL: str = "sqlite+aiosqlite:///short.db"
    TOKEN_SIGN_SECRET: str = "dasfasdfasdfas"


@lru_cache
def get_settings():
    return Settings()
