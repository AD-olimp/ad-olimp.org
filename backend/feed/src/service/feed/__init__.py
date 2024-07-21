from .service import FeedService


def get_feed_service() -> FeedService:
    return FeedService()


__all__ = ['FeedService', 'get_feed_service']
