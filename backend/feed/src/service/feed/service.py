from fastapi import Depends

from difflib import SequenceMatcher

from .interface import FeedServiceInterface
from src.repository import RepositoryInterface, get_repository
from src.database.uow import UnitOfWork

from src.models.feeds import GetFeedDTO, PublicationFilterDTO
from src.models.publication import PublicationDTO


class FeedService(FeedServiceInterface):
    """Сервис для работы с лентой постов"""
    
    confidence_interval = 0.8
    
    def __init__(self, UoW: UnitOfWork, Repo: RepositoryInterface = Depends(get_repository)):
        self.uow = UoW
        self.repo = Repo

    async def get_feeds(self, feed_filter: GetFeedDTO) -> list[PublicationDTO]:
        async with self.uow as uow:
            return await self.repo.get_all(feed_filter, uow.session)
    
    @classmethod
    def _is_similar(cls, text1, text2):
        return SequenceMatcher(None, text1, text2) >= cls.confidence_interval

    async def search_feeds(self, feed_filter: PublicationFilterDTO, search_text: str) -> list[PublicationDTO]:
        async with self.uow as uow:
            return [
                p async for p in await self.repo.get_all(feed_filter, uow.session)
                if self._is_similar(search_text, p['text'])
            ]
