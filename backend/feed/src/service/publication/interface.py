from bson import ObjectId
from abc import ABC, abstractmethod


class PublicationServiceInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""

    @abstractmethod
    async def create_publication(self, publication):
        ...

    @abstractmethod
    async def get_publication_by_id(self, publication_id: ObjectId):
        ...
        
    @abstractmethod
    async def update_publication(self, publication_id: ObjectId, new_publication):
        ...

    @abstractmethod
    async def delete_publication(self, publication_id: ObjectId):
        ...
