import threading
from fastapi import FastAPI
from fastapi import APIRouter
import time
import asyncio

app = FastAPI(
    title="Learning demo", description="Learning fastapi", version="0.0.1", debug=False
)


@app.get("/sync")
def sync_func():
    time.sleep(2)
    print(threading.get_ident())
    return {"index": "sync"}


@app.get("/async")
async def async_func():
    await asyncio.sleep(2)
    print(threading.get_ident())
    return {"index": "async"}
