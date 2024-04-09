from functools import lru_cache
from pydantic_settings import BaseSettings


class SettingsA(BaseSettings):
    debug: bool = False
    title: str
    description: str
    version: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class SettingsB(BaseSettings):
    debug: bool = False
    title: str
    description: str
    version: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    print("get 1111")
    return SettingsB()


if __name__ == "__main__":
    settingsA = SettingsA()
    print(settingsA.debug)
    print(settingsA.title)
    print(settingsA.description)
    print(settingsA.version)

    b = get_settings()
    print(b.debug)
    print(b.title)
    print(b.description)
    print(b.version)

    c = get_settings()
    print(c.debug)
    print(c.title)
    print(c.description)
    print(c.version)
