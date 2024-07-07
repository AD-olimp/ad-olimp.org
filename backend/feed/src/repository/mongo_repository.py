from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection

from dataclasses import asdict
from .interface import RepositoryInterface

from src.models import PublicationDTO, PublicationFilterDTO, GetFeedDTO


class MongoRepositoryPublications(RepositoryInterface):
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create(
            self,
            session: AsyncIOMotorClientSession,
            publication: PublicationDTO
    ) -> str:
        await self.collection.insert_one(
            document=asdict(publication),
            session=session
        )

    async def get(
            self,
            session: AsyncIOMotorClientSession,
            publication_filter: PublicationFilterDTO
    ) -> PublicationDTO:

        return await self.collection.find_one(
            document=asdict(publication_filter),
            session=session
        )

    async def get_all(
            self, session: AsyncIOMotorClientSession,
            publication_filter: PublicationFilterDTO
    ) -> GetFeedDTO:

        response = await self.collection.find(
            document=asdict(publication_filter),
            session=session
        )
        print(response)

        return response

    async def update(
            self,
            session: AsyncIOMotorClientSession,
            publication_filter: PublicationFilterDTO,
            new_publication: PublicationDTO
    ) -> bool:

        await self.collection.update_one(
            asdict(publication_filter),
            update={'$set': new_publication},
            session=session
        )

    async def delete(
            self,
            session: AsyncIOMotorClientSession,
            publication_filter: PublicationFilterDTO
    ) -> bool:

        await self.collection.delete_one(asdict(publication_filter))
