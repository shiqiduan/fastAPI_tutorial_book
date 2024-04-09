import threading
from fastapi import FastAPI
from fastapi import APIRouter
import time
import asyncio

from fastapi.responses import JSONResponse

app = FastAPI(
    title="主应用", description="Learning fastapi", version="0.0.1", debug=False
)


@app.get("/index", summary="首页")
async def index():
    return JSONResponse({"index": "主入口"})


subapp = FastAPI(title="子应用", description="子应用的描述", ersion="2.0.0")


@subapp.get("/index", summary="首页")
async def index():
    return JSONResponse({"index": "子入口"})


app.mount("/subapp", subapp, name="子应用")
