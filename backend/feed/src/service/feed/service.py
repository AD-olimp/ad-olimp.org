from .interface import FeedServiceInterface
from src.repository.mongo_repository import MongoRepository

from src.models.feeds import GetFeedDTO
from src.models.publication import FeedListDTO

class FeedService(FeedServiceInterface):
    
    @classmethod
    async def get_feeds(repo: MongoRepository, feed_filter: GetFeedDTO) -> FeedListDTO:
        return await repo.get_all(feed_filter)
        