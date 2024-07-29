from bson import ObjectId
from typing import Optional, Any
from .interface import RepositoryInterface
from src.models import Publication, GetFeed, PublicationFilter
from ..database import AsyncMongoDB
from ..models.feeds import GetSearch
from ..service.mapper.feed import transform_filter, get_query


class PublicationsMongoRepository(RepositoryInterface):
    async def add(self, session: AsyncMongoDB, new_publication: Publication) -> None:
        result = await session.pub_collection.insert_one(new_publication.dict())
        return result.inserted_id

    async def get(self, session: AsyncMongoDB, publication_filter: dict[Any]) -> Publication:
        return Publication(**(
            await session.pub_collection.find_one(publication_filter)
        ))

    async def get_by_filter(self, session: AsyncMongoDB, publication_filters: GetFeed) -> list[Optional[Publication]]:
        # Просто для получения ленты
        session.pub_collection.create_index({"text": "text"})
        result = await (session.pub_collection.find(transform_filter(publication_filters))
                        .to_list(length=publication_filters.end))

        return [Publication(**pub) for pub in result]

    async def search_by_text(
            self,
            session: AsyncMongoDB,
            search_filter: GetSearch
    ) -> list[Optional[Publication]]:
        base_query, score_query = get_query(search_filter)
        result = await (session.pub_collection.find(base_query, score_query)
                        .sort({"score": {"$meta": "textScore"}}).to_list(length=search_filter.end))

        return [
            Publication(
                text=pub['text'],
                title=pub['title'],
                tags=pub['tags'],
                pictures_path=pub['pictures_path'],
                data=pub['data']
            ) for pub in result
        ]

    async def update(self, session: AsyncMongoDB, publication_id: ObjectId, new_publication: Publication) -> None:
        await session.pub_collection.update_one({"_id": publication_id}, {'$set': new_publication.dict()})

    async def delete(self, session: AsyncMongoDB, publication_id: ObjectId) -> None:
        await session.pub_collection.delete_one({'_id': publication_id})
