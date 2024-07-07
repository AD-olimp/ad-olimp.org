from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""
    @abstractmethod
    def __init__(self, collection):
        ...

    @abstractmethod
    async def create(self, session, item):
        ...
    
    @abstractmethod
    async def get(self, session, item_id: str):
        ...
        
    @abstractmethod
    async def get_all(self, session, item_id: str):
        ...
        
    @abstractmethod
    async def update(self, session, item_id: str, new_item):
        ...

    @abstractmethod
    async def delete(self, session, item_id: str):
        ...
