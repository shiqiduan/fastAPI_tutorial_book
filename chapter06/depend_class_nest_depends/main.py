from typing import Tuple
from fastapi import FastAPI, Query
from fastapi import HTTPException
from fastapi import Depends


app = FastAPI()


def username_check(username: str = Query(...)):
    if username != "admin":
        raise HTTPException(status_code=403, detail="username is not valid")
    return username


def age_check(username: str = Depends(username_check), age: int = Query(...)):
    if age < 18:
        raise HTTPException(status_code=403, detail="age is not valid")
    return username, age


def other_check(other: str = Query(...)):
    if other != "other":
        raise HTTPException(status_code=403, detail="other is not valid")
    return other


@app.get("/user/login")
def user_login(
    username_and_age: Tuple = Depends(age_check), other: str = Depends(other_check)
):
    return {"username": username_and_age[0], "age": username_and_age[1], "other": other}


@app.get("/user/info")
def user_info(
    username_and_age: Tuple = Depends(age_check), other: str = Depends(other_check)
):
    return {"username": username_and_age[0], "age": username_and_age[1], "other": other}


# Depends 与 validator 的关系是什么呢?
# why 这么设计
# 这算不上依赖注入吧
