"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session                                             +
добавьте модели User и Post, объявите поля:                         +
для модели User обязательными являются name, username, email        +
для модели Post обязательными являются user_id, title, body         +
создайте связи relationship между моделями: User.posts и Post.user  +
"""

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, declared_attr, scoped_session, relationship

import os

from homework_04 import config

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:userpass@localhost/postgres"


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

async_engine = create_async_engine(
    url=config.DB_ASYNC_URL,
    echo=config.DB_ECHO
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


Base = declarative_base(bind=async_engine, cls=Base)


Session = async_session

class User(Base):
    name = Column(String(60), nullable=False)
    username = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user", uselist=True)


    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"user={self.name!r} {self.username!r}"
            ")"
        )

    def __repr__(self):
        return str(self)

class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=False
    )

    title = Column(
        String(120),
        nullable=False
    )
    body = Column(
        String(300),
        nullable=False
    )

    user = relationship("User", back_populates="posts", uselist=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"title={self.title!r}"
            ")"
        )

    def __repr__(self):
        return str(self)


