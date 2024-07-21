from bson import ObjectId
from typing import Optional, Any
from motor.motor_asyncio import AsyncIOMotorDatabase

from .interface import RepositoryInterface
from .validation import exist_validation
from src.models import Publication
from src.config import MongoDBConfig


class PublicationsMongoRepository(RepositoryInterface):
    def __init__(self, database: AsyncIOMotorDatabase):
        self.collection = database[MongoDBConfig.publications_collection]

    async def add(self, session, new_publication: Publication) -> None:
        await self.collection.insert_one(new_publication.dict(), session=session)

    @exist_validation(raise_if_exists=False)
    async def get(self, session, publication_filter: dict[Any]) -> Publication:
        return Publication(**(
            await self.collection.find_one(publication_filter, session=session)
        ))

    async def get_all(self, session, publication_filters: dict[Any]) -> list[Optional[Publication]]:
        return [
            Publication(**pub) for pub in
            await self.collection.find(publication_filters, session=session)
        ]

    @exist_validation(raise_if_exists=False)
    async def update(self, session, publication_id: ObjectId, new_publication: Publication) -> None:
        await self.collection.update_one(session, {"_id": publication_id}, {'$set': new_publication})

    @exist_validation(raise_if_exists=False)
    async def delete(self, session, publication_id: ObjectId) -> None:
        await self.collection.delete_one(session, {'_id': publication_id})
