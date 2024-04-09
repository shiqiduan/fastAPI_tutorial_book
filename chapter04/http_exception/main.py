from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code, content=exc.detail, headers=exc.headers
    )


@app.get("/http_exception")
async def http_exception(action_scopes: str = Query(default="admin")):
    if action_scopes == "admin":
        raise HTTPException(
            status_code=403,
            headers={"X-auth": "No AUTH"},
            detail={"code": 403, "message": "你没有权限", "aaa": "cccc"},
        )
    return {"code": "200"}
