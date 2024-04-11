import copy
from fastapi import APIRouter, Depends
from schemas.user import UserCreate
from models.user import User
from db.database import get_db_session, AsyncSession
from services.user import UserService


router_user = APIRouter(prefix="/api/v1/user", tags=["user"])


@router_user.post("/create")
async def create(user: UserCreate, db_session: AsyncSession = Depends(get_db_session)):
    u = User()
    u.name = user.name
    u.nikename = user.nikename
    u.password = user.password
    u.email = user.email
    result = await UserService.create_user(db_session, u)
    return {"code": 200, "message": "用户创建成功", "data": result}


@router_user.get("/info")
async def info(name: str, db_session: AsyncSession = Depends(get_db_session)):
    result = await UserService.get_user_by_name(db_session, name)
    return {"code": 200, "message": "查询用户信息成功", "data": result}


@router_user.get("/user/list")
async def list(db_session: AsyncSession = Depends(get_db_session)):
    result = await UserService.get_users(db_session)
    return {"code": 200, "message": "查询用户列表成功", "data": result}


@router_user.put("/edit")
async def edit():
    return {"code": 200, "message": "修改用户信息成功"}


@router_user.delete("/create")
async def delete():
    return {"code": 200, "message": "删除用户信息成功"}
