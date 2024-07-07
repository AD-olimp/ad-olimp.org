from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession, AsyncIOMotorCollection
from src.config import MongoDBConfig


class UnitOfWork:
    def __init__(self, client: AsyncIOMotorClient, db_name: str):
        self.client = client
        self.db_name = db_name
        self.session: AsyncIOMotorClientSession = None

    async def __aenter__(self):
        self.session = await self.client.start_session()
        self.session.start_transaction()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            await self.session.commit_transaction()
        else:
            await self.session.abort_transaction()
        await self.session.end_session()

    async def commit(self):
        await self.session.commit_transaction()

    async def rollback(self):
        await self.session.abort_transaction()

    @property
    def db(self):
        return self.client[self.db_name]

    @property
    def collection(self) -> AsyncIOMotorCollection:
        return self.client[self.db_name][MongoDBConfig.collection]


def get_uow() -> UnitOfWork:
    return UnitOfWork(
        client=AsyncIOMotorClient(MongoDBConfig.url),
        db_name=MongoDBConfig.database
    )
