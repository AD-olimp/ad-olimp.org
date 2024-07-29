from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import configuration


async_engine: AsyncEngine = _create_async_engine(
    url=configuration.db.build_connection_str(),
    echo=configuration.debug,
    pool_pre_ping=True
)


AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


@asynccontextmanager
async def get_session():
    async with AsyncSessionLocal() as session:
        try:
            # Выполняю транзакцию
            yield session
            await session.commit()

        except Exception:
            # В случае ошибки откатываю все назад
            await session.rollback()
            raise

        finally:
            # В любом случае закрываю соединение
            await session.close()
