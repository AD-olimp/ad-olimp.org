from bson import ObjectId
from typing import Optional, Any
from .interface import RepositoryInterface
from src.models import Publication
from ..database import AsyncMongoDB


class PublicationsMongoRepository(RepositoryInterface):
    async def add(self, session: AsyncMongoDB, new_publication: Publication) -> None:
        await session.pub_collection.insert_one(new_publication.dict())

    async def get(self, session: AsyncMongoDB, publication_filter: dict[Any]) -> Publication:
        return Publication(**(
            await session.pub_collection.find_one(publication_filter)
        ))

    async def get_all(self, session: AsyncMongoDB, publication_filters: dict[Any]) -> list[Optional[Publication]]:
        return [
            Publication(**pub) for pub in
            await session.pub_collection.find(publication_filters)
        ]

    async def update(self, session: AsyncMongoDB, publication_id: ObjectId, new_publication: Publication) -> None:
        await session.pub_collection.update_one({"_id": publication_id}, {'$set': new_publication.dict()})

    async def delete(self, session: AsyncMongoDB, publication_id: ObjectId) -> None:
        await session.pub_collection.delete_one({'_id': publication_id})
