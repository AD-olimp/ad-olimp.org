from fastapi import Depends
from difflib import SequenceMatcher

from src.models.feeds import GetFeed, GetSearch
from .interface import FeedServiceInterface
from src.database import get_db
from src.models.publication import Publication
from src.repository import RepositoryInterface, get_repository


class FeedService(FeedServiceInterface):
    """Сервис для работы с лентой постов"""
    
    confidence_interval = 0.8
    
    def __init__(self):
        self.repo: RepositoryInterface = get_repository()

    async def get_feeds(self, feeds_filter: GetFeed):
        async with get_db() as session:
            await self.repo.get_by_filter(
                session=session, publication_filters=feeds_filter.publication_filter.dict()
            )

    async def get_search(self, search_filter: GetSearch):
        async with get_db() as session:
            await self.repo.search_by_text(
                session=session,
                text=search_filter.search_filter.text,
                publication_filters=search_filter.search_filter.dict()
            )