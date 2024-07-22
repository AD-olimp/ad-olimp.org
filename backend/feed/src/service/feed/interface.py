from abc import ABC, abstractmethod
from src.models.feeds import GetFeed


class FeedServiceInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""

    @abstractmethod
    async def get_feeds(self, feeds_filter: GetFeed, search_result):
        ...
