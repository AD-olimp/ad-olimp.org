from pymongo import MongoClient
from .interface import RepositoryInterface

from src.models import PublicationDTO, PublicationFilterDTO, GetFeedDTO


class MongoRepository(RepositoryInterface):
    def __init__(
            self,
            client: MongoClient,
            db_name: str,
            collection_name: str
        ):
        
        self.db = client[db_name]
        self.collection = self.db[collection_name]

    async def create(
            self,
            publication: PublicationDTO
        ) -> str:        
        
        return str(
            self.collection\
                .insert_one(publication)\
                .inserted_id
        )

    async def get(
            self,
            publication_filter: PublicationFilterDTO
        ) -> PublicationDTO:
        
        return self.collection.find_one(publication_filter)

    async def get_all(
            self,
            publication_filter: PublicationFilterDTO
        ) -> GetFeedDTO:
        
        return GetFeedDTO(self.collection.find(publication_filter))

    async def update(
            self,
            publication_filter: PublicationFilterDTO,
            new_publication: PublicationDTO
        ) -> bool:
        
        result = self.collection.update_one(publication_filter, {'$set': new_publication})
        return result.modified_count > 0

    async def delete(
            self,
            publication_filter: PublicationFilterDTO,
        ) -> bool:
        
        result = self.collection.delete_one(publication_filter)
        return result.deleted_count > 0
