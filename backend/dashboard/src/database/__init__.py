from contextlib import asynccontextmanager
from src.database.models.session import AsyncMongoDB


@asynccontextmanager
async def get_db() -> AsyncMongoDB:
    yield AsyncMongoDB()


async def ping_mongodb():
    ...


__all__ = ['get_db', 'AsyncMongoDB']
