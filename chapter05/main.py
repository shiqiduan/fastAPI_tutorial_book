from fastapi import Depends, FastAPI
from pydantic import (
    BaseModel,
    ValidationError,
    model_validator,
    root_validator,
    Field,
    ValidationError,
)

app = FastAPI()


class User(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=20,
    )
    password_old: str = Field(
        ...,
        title="旧密码",
        description="密码需要大于 6",
        min_length=6,
        examples=["123"],
    )
    password_new: str = Field(
        ..., title="新密码", description="密码需要大于 6", min_length=6
    )

    @model_validator(mode="before")
    @classmethod
    def validate_password(cls, values):
        password_old = values.get("password_old")
        password_new = values.get("password_new")
        if password_old and password_new and password_old != password_new:
            raise ValueError("Passwords do not match")
        return values


# https://github.com/tiangolo/fastapi/issues/1474
@app.get("/user")
def read_user(user: User = Depends()):
    return {
        "username": user.username,
        "password_old": user.password_old,
        "password_new": user.password_new,
    }
