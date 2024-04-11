from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import declarative_base, sessionmaker

from config.config import get_settings

# 创建异步引擎对象
async_engine = create_async_engine(get_settings().ASYNC_DATABASE_URI, echo=False)

# 创建 ORM 模型基类
Base = declarative_base()

# 创建异步会话管理对象
sessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    db_session = None
    try:
        db_session = sessionLocal()
        yield db_session
    finally:
        await db_session.close()
