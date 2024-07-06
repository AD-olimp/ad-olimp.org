from abc import ABC, abstractmethod


class FeedServiceInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""
    
    
    @classmethod
    @abstractmethod
    async def get_feeds(session, feeds_filter):
        ...
