from difflib import SequenceMatcher

from .interface import FeedServiceInterface
from src.repository.interface import RepositoryInterface

from src.models.feeds import GetFeedDTO
from src.models.publication import PublicationDTO

class FeedService(FeedServiceInterface):
    """Сервис для работы с лентой постов"""
    
    confidence_interval = 0.8
    
    def __init__(self, repo: RepositoryInterface):
        self._repo = repo
    
    async def get_feeds(self, feed_filter: GetFeedDTO) -> list[PublicationDTO]:
        return await self._repo.get_all(feed_filter)
    
    @classmethod
    def _is_similar(cls, text1, text2):
        return SequenceMatcher(None, text1, text2) >= cls.confidence_interval
    
    async def search_feeds(self, feed_filter: GetFeedDTO, search_text: str) -> list[PublicationDTO]:
        return [p for p in await self._repo.get_all(feed_filter) if self._is_similar(search_text, p.text)]
        