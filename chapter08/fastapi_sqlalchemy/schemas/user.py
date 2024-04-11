from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str
    nikename: str
    email: str
