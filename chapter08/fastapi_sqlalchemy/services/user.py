from sqlalchemy import delete, select, update
from db.database import async_engine, Base
from models.user import User
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:

    @staticmethod
    async def init_create_table():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def get_user(async_session: AsyncSession, user_id: int):
        result = await async_session.execute(select(User).where(User.id == user_id))
        return result.scalars().first()

    @staticmethod
    async def get_user_by_name(async_session: AsyncSession, name: str):
        result = await async_session.execute(select(User).where(User.name == name))
        return result.scalars().first()

    @staticmethod
    async def get_users(async_session: AsyncSession, skip: int = 0, limit: int = 100):
        result = await async_session.execute(
            select(User).offset(skip).limit(limit).order_by(User.id)
        )
        return result.scalars().all()

    @staticmethod
    async def create_user(async_session: AsyncSession, user: User):
        async_session.add(user)
        await async_session.commit()
        await async_session.refresh(user)
        return user

    @staticmethod
    async def update_user(async_session: AsyncSession, user: User):
        response = update(User).where(User.id == user.id).values(user.dict())
        result = await async_session.execute(response)
        await async_session.commit()
        return result

    @staticmethod
    async def delete_user(async_session: AsyncSession, user_id: int):
        response = delete(User).where(User.id == user_id)
        result = await async_session.execute(response)
        await async_session.commit()
        return result
