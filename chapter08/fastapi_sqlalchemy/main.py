from fastapi import FastAPI
from services.user import UserService
from contextlib import asynccontextmanager


async def startup_event():
    print("Starting up...")
    await UserService.init_create_table()


async def shutdown_event():
    print("Shutting down...")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_event()
    yield
    await shutdown_event()


app = FastAPI(lifespan=lifespan)
