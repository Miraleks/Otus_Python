"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()

        return data

async def get_users() -> list[dict]:
    users = await fetch_json(USERS_DATA_URL)
    return users

async def get_posts() -> list[dict]:
    posts = await fetch_json(POSTS_DATA_URL)
    return posts