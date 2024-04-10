from fastapi import FastAPI, Request
from fastapi import Query, Depends
from fastapi.exceptions import HTTPException
from fastapi import Body

app = FastAPI()


def username_check(username: str = Query(...)):
    if username != "admin":
        raise HTTPException(status_code=401, detail="Invalid username")
    return username


# @app.get("/user/login/")
# def user_login(username: str = Depends(username_check)):
#     return username


# @app.get("/user/info/")
# def user_info(username: str = Depends(username_check)):
#     return username


# class UsernameCheck:
#     def __init__(self, username: str = Query(...)):
#         if username != "admin":
#             raise HTTPException(status_code=401, detail="Invalid username")
#         self.username = username


# @app.get("/user/login/")
# def user_login(username: UsernameCheck = Depends(UsernameCheck)):
#     return username


# @app.get("/user/info/")
# def user_info(username: UsernameCheck = Depends(UsernameCheck)):
#     return username


class UsernameCheck:
    def __init__(self, password: str):
        self.password = password

    def username_form_query(self, username: str = Query(...)):
        if username != "admin":
            raise HTTPException(status_code=401, detail="Invalid username from query")
        return username

    def username_form_post(self, username: str = Body(...)):
        if username != "admin":
            raise HTTPException(status_code=401, detail="Invalid username from body")
        return username


upw = UsernameCheck(password="123456")


@app.get("/user/login/")
def user_login(username: UsernameCheck = Depends(upw.username_form_query)):
    return username


@app.post("/user/info")
def user_info(username: UsernameCheck = Depends(upw.username_form_post)):
    return username
