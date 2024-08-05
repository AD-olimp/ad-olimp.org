import asyncio
from dataclasses import asdict

from src.app import App
from src.config import configuration
from src.api.v1 import router_v1
from src.database.session import async_engine
from src.models.orm.base import metadata


def main():
    return App(host='0.0.0.0', port=8000, **asdict(configuration.app)) \
        .included_cors() \
        .included_routers(routers=[router_v1])


def do_migration():
    async def init_models():
        async with async_engine.begin() as conn:
            await conn.run_sync(metadata.drop_all)
            await conn.run_sync(metadata.create_all)

    asyncio.run(init_models())


if __name__ == '__main__':
    main()
