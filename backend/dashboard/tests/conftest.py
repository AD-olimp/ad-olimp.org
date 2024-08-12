import asyncio
import os
import logging
from typing import Optional
import pytest

from dotenv import load_dotenv
from dataclasses import dataclass, field
from sqlalchemy.engine import URL

from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from src.models.orm.base import metadata

dotenv_path = os.path.join(os.path.dirname(__file__), '../.test.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


@dataclass
class TestNGINXConfig:
    APP_PREFIX: str = os.getenv("APP_NGINX_PREFIX")


@dataclass
class TestDatabaseConfig:
    """Database connection variables."""

    name: Optional[str] = os.getenv('TEST_POSTGRES_DATABASE')
    user: Optional[str] = os.getenv('TEST_POSTGRES_USER')
    password: Optional[str] = os.getenv('TEST_POSTGRES_PASSWORD', None)
    port: int = int(os.getenv('TEST_POSTGRES_PORT', 5432))
    host: str = os.getenv('TEST_POSTGRES_HOST', 'db')

    driver: str = 'asyncpg'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        """This function build a connection string."""

        return URL.create(
            drivername=f'{self.database_system}+{self.driver}',
            username=self.user,
            database=self.name,
            password=self.password,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class TestAppConfig:
    """Bot configuration."""

    title = "ad-olimp.org publications"
    description = "Сервис для работы с публикациями в ленту"
    version = "1.0"
    root_path = TestNGINXConfig.APP_PREFIX


@dataclass
class TestConfiguration:
    """All in one configuration's class."""

    debug = bool(os.getenv('DEBUG'))
    logging_level = int(os.getenv('LOGGING_LEVEL', logging.INFO))

    db = TestDatabaseConfig()
    app = TestAppConfig()


test_configuration = TestConfiguration()


test_async_engine: AsyncEngine = _create_async_engine(
    url=test_configuration.db.build_connection_str(),
    echo=True,
    pool_pre_ping=True
)


TestAsyncSessionLocal = async_sessionmaker(
    bind=test_async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


@asynccontextmanager
async def get_session_test():
    async with TestAsyncSessionLocal() as session:
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


async def init_models():
    async with test_async_engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


@pytest.fixture(scope="session")
def setup_db():
    print("MIGRATION")
    # asyncio.run(init_models())


@pytest.fixture(scope='session')
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
