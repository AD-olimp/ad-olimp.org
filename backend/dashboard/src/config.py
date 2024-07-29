import os
import logging
from typing import Optional

from dotenv import load_dotenv
from dataclasses import dataclass, field
from sqlalchemy.engine import URL


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


@dataclass
class NGINXConfig:
    APP_PREFIX: str = os.getenv("APP_NGINX_PREFIX")


@dataclass
class DatabaseConfig:
    """Database connection variables."""

    name: Optional[str] = os.getenv('POSTGRES_DATABASE')
    user: Optional[str] = os.getenv('POSTGRES_USER')
    password: Optional[str] = os.getenv('POSTGRES_PASSWORD', None)
    port: int = int(os.getenv('POSTGRES_PORT', 5432))
    host: str = os.getenv('POSTGRES_HOST', 'db')

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
class AppConfig:
    """Bot configuration."""

    title = "ad-olimp.org publications"
    description = "Сервис для работы с публикациями в ленту"
    version = "1.0"
    root_path = NGINXConfig.APP_PREFIX


@dataclass
class Configuration:
    """All in one configuration's class."""

    debug = bool(os.getenv('DEBUG'))
    logging_level = int(os.getenv('LOGGING_LEVEL', logging.INFO))

    db = DatabaseConfig()
    app = AppConfig()


configuration = Configuration()
