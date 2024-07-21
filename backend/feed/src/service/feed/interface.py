from abc import ABC, abstractmethod


class FeedServiceInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""

    @abstractmethod
    async def get_feeds(self, session, feeds_filter):
        ...
