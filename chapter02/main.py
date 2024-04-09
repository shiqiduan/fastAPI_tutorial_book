import pathlib
import time
from fastapi import BackgroundTasks, FastAPI, Request
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Learning demo", description="Learning fastapi", version="0.0.1", debug=False
)

templates = Jinja2Templates(directory=f"{pathlib.Path.cwd()}/templates/")
staticfiles = StaticFiles(directory=f"{pathlib.Path.cwd()}/static/")
app.mount("/static", staticfiles, name="static")


@app.get("/app/hello", tags=["示例"])
def app_hello():
    return "Hello world"


@app.get("/", tags=["首页"], response_class=HTMLResponse)
async def get_response(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/task")
async def run_task(tasks: BackgroundTasks):
    tasks.add_task(print, "Hello world")
    tasks.add_task(send_mail, 5)
    return "Hello world"


def send_mail(n):
    time.sleep(n)
    print("send_mail")


@app.on_event("startup")
async def startup_event_async():
    print("startup_event_async")


@app.on_event("startup")
def startup_event_sync():
    print("startup_event_sync")


@app.on_event("shutdown")
def shutdown_event():
    print("shutdown_event")
