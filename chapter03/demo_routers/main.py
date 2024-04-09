from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute


async def fastapi_index():
    return JSONResponse({"index": "fastapi_index"})


async def fastapi_about():
    return JSONResponse({"about": "fastapi_about"})


routes = [
    APIRoute(path="/fastapi/index", endpoint=fastapi_index, methods=["GET", "POST"]),
    APIRoute(path="/fastapi/about", endpoint=fastapi_about, methods=["GET", "POST"]),
]

app = FastAPI(routes=routes)
