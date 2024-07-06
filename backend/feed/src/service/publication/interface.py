from abc import ABC, abstractmethod


class PublicationServiceInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""
    
    
    @classmethod
    @abstractmethod
    async def create_publication(session, publication):
        ...
    
    
    @classmethod
    @abstractmethod
    async def get_publication(session, publication_id: str):
        ...
        
        
    @classmethod
    @abstractmethod
    async def update_publication(session, publication_id: str, new_publication):
        ...
    
    
    @classmethod
    @abstractmethod
    async def delete_publication(session, publication_id: str):
        ...
