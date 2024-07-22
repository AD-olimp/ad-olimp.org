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

    async def get_by_filter(self, session: AsyncMongoDB, publication_filters: dict[Any]) -> list[Optional[Publication]]:
        # Просто для получения ленты
        result = await session.pub_collection.find(publication_filters).to_list(5)

        print(list(result))

        return [Publication(**pub) for pub in result]

    async def search_by_text(
            self,
            session: AsyncMongoDB,
            text: str,
            publication_filters: dict[Any]
    ) -> list[Optional[Publication]]:
        # Для получения ленты с поиском по тексту

        result = session.pub_collection.find(
            {"$text": {"$search": text}}, {"score": {"$meta": "textScore"}}
        ).sort({"score": {"$meta": "textScore"}})

        return [
            Publication(
                text=pub['text'],
                title=pub['title'],
                tags=pub['tags'],
                pictures_path=pub['pictures_path'],
                data=pub['data']
            ) for pub in await result.to_list(5)
        ]

    async def update(self, session: AsyncMongoDB, publication_id: ObjectId, new_publication: Publication) -> None:
        await session.pub_collection.update_one({"_id": publication_id}, {'$set': new_publication.dict()})

    async def delete(self, session: AsyncMongoDB, publication_id: ObjectId) -> None:
        await session.pub_collection.delete_one({'_id': publication_id})
