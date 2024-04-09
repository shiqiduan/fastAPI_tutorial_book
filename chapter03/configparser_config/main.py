from fastapi import FastAPI
import configparser


config = configparser.ConfigParser()
config.read("conf.ini", encoding="utf-8")

app = FastAPI(
    debug=bool(config.get("fastapi_config", "debug")),
    title=config.get("fastapi_config", "title"),
    description=config.get("fastapi_config", "description"),
    version=config.get("fastapi_config", "version"),
)
