from abc import ABC, abstractmethod

from src.models import PublicationDTO, PublicationFilterDTO


class RepositoryInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""
    @abstractmethod
    def __init__(self, collection):
        ...

    @abstractmethod
    async def create(self, session, publication: PublicationDTO):
        ...
    
    @abstractmethod
    async def get(self, session, publication_filter: PublicationFilterDTO):
        ...
        
    @abstractmethod
    async def get_all(self, session, publication_filter: PublicationFilterDTO):
        ...
        
    @abstractmethod
    async def update(self, session, publication_filter: PublicationFilterDTO, new_publication: PublicationDTO):
        ...

    @abstractmethod
    async def delete(self, session, publication_filter: PublicationFilterDTO):
        ...
