"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
import platform
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession


from homework_04.models import User, Post, Base, async_engine, Session
from homework_04.jsonplaceholder_requests import get_users, get_posts


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def fetch_users_data() -> list[User]:
    users = await get_users()
    users_list = []
    for user in users:
        new_user = User(name=user['name'], username=user['username'], email=user['email'])
        users_list.append(new_user)

    return users_list


async def fetch_posts_data() -> list[Post]:
    posts = await get_posts()
    posts_list = []
    for post in posts:
        new_post = Post(user_id=post['userId'], title=post['title'], body=post['body'])
        posts_list.append(new_post)

    return posts_list


async def create_users(session: AsyncSession, users: list[User]):
    session.add_all(users)
    await session.commit()



async def create_posts(session: AsyncSession, posts: list[Post]):
    session.add_all(posts)
    await session.commit()

async def async_main():
    users_data: List[User]
    posts_data: List[Post]

    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with Session() as session:
        await create_users(session, users_data)
        await create_posts(session, posts_data)


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())