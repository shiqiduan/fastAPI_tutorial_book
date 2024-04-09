from fastapi import FastAPI
from starlette.responses import JSONResponse


async def exception_not_found(request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "不存在的地方"},
    )


exception_handlers = {
    404: exception_not_found,
}

app = FastAPI(exception_handlers=exception_handlers)
