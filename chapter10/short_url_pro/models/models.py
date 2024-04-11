from db.database import Base
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, func


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime(), default=func.now())


class ShortUrl(Base):
    __tablename__ = "short_urls"
    id = Column(Integer, primary_key=True, index=True)
    short_tag = Column(String(20), nullable=False)
    short_url = Column(String(100), nullable=False)
    long_url = Column(String, nullable=False)
    visits_count = Column(Integer, default=0)
    created_at = Column(DateTime(), default=func.now())
    created_by = Column(String(20))
    msg_context = Column(String, nullable=False)
