from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""
    
    @classmethod
    @abstractmethod
    async def create(session, item):
        ...
    
    @classmethod
    @abstractmethod
    async def get(session, item_id: str):
        ...
        
    @classmethod
    @abstractmethod
    async def get_all(session, item_id: str):
        ...
        
    @classmethod
    @abstractmethod
    async def update(session, item_id: str, new_item):
        ...
    
    @classmethod
    @abstractmethod
    async def delete(session, item_id: str):
        ...
