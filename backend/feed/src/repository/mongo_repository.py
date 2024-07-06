from pymongo import MongoClient
from dataclasses import asdict
from .interface import RepositoryInterface

from src.models import PublicationDTO, PublicationFilterDTO, GetFeedDTO


class MongoRepositoryPublications(RepositoryInterface):
    def __init__(
            self,
            client: MongoClient,
            db_name: str,
            collection_name: str
        ):
        
        self.db = client[db_name]
        self.collection = self.db[collection_name]

    async def create(self, publication: PublicationDTO) -> str:
        return str(
            self.collection\
                .insert_one(asdict(publication))\
                .inserted_id
        )

    async def get(self, publication_filter: PublicationFilterDTO) -> PublicationDTO:
        return self.collection.find_one(asdict(publication_filter))

    async def get_all(self, publication_filter: PublicationFilterDTO) -> GetFeedDTO:
        return GetFeedDTO(**self.collection.find(publication_filter))

    async def update(self, publication_filter: PublicationFilterDTO, new_publication: PublicationDTO) -> bool:
        result = self.collection.update_one(publication_filter, {'$set': new_publication})
        return result.modified_count > 0

    async def delete(self, publication_filter: PublicationFilterDTO) -> bool:
        result = self.collection.delete_one(asdict(publication_filter))
        return result.deleted_count > 0
