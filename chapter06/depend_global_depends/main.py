from typing import Tuple
from fastapi import FastAPI, Query
from fastapi import HTTPException
from fastapi import Depends


def username_check(username: str = Query(...)):
    if username != "admin":
        raise HTTPException(status_code=403, detail="username is not valid")
    return username


def age_check(age: int = Query(...)):
    if age < 18:
        raise HTTPException(status_code=403, detail="age is not valid")
    return age


app = FastAPI(dependencies=[Depends(username_check), Depends(age_check)])


@app.get("/user/login")
def user_login():
    return {"username": "login", "age": 18}


@app.get("/user/info")
def user_info():
    return {"username": "info", "age": 18}


from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/user/apirouter/")
def user_apirouter():
    return {"username": "router", "age": 18}
