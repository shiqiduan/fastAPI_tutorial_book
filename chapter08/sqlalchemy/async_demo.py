import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Integer, String, Column, select
from sqlalchemy.ext.asyncio import AsyncSession

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///aiosqlite_user.db"
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    nikename = Column(String)
    password = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, nikename={self.nikename}, password={self.password}, email={self.email})>"


async def init_create():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_user(async_session, user_id):
    ret = await async_session.execute(select(User).where(User.id == user_id))
    return ret.scalars().first()


async def get_user_by_name(async_session, name):
    ret = await async_session.execute(select(User).where(User.name == name))
    return ret.scalars().first()


async def create_user(async_session, name, nikename, email, password):
    user = User(name=name, nikename=nikename, email=email, password=password)
    async_session.add(user)
    await async_session.commit()
    return user


async def test_run():
    async_session = sessionmaker(
        autocommit=False, bind=async_engine, class_=AsyncSession
    )()
    user = await create_user(async_session, "test", "test", "test", "test")
    # ???
    print(str(user))
    user = await get_user(async_session, 1)
    print(str(user))
    await async_session.close()


asyncio.run(init_create())
asyncio.run(test_run())
