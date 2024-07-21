from motor.motor_asyncio import AsyncIOMotorClient

from src.config import MongoDBConfig


class AsyncMongoDB:
    client = AsyncIOMotorClient(MongoDBConfig.url)
    database = client[MongoDBConfig.database]
    pub_collection = database[MongoDBConfig.publications_collection]

    def __init__(self):
        # Сессия БД. будет создаваться каждый раз в конструкции
        # async with AsyncSession as session ...
        self.session = None

    async def __aenter__(self):
        self.session = await self.client.start_session()  # Создаем сессию
        self.session.start_transaction()  # Начинаем сессию

        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.session.abort_transaction()  # Если есть ошибка, то откатывается назад

        else:
            await self.session.commit_transaction()  # Иначе коммитим изменения

        # В любом случае закрываем сессию
        await self.session.end_session()


