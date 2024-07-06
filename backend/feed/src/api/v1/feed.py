from fastapi import APIRouter

from .schemas.feed import PublicationFilter, GetFeed, FeedResponse

from src.service.feed.service import FeedService
from src.models.feeds import GetFeedDTO, PublicationFilterDTO
from src.models.publication import FeedListDTO

feed_router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)


# TODO: как делать гет запросы 
@feed_router.get("/feed/{feed_filter}")
async def get_feed(feed_filter: GetFeed) -> FeedResponse:
    
    feed_filter = GetFeedDTO(
        start=feed_filter.start,
        end=feed_filter.end,
        publication_filter=PublicationFilterDTO(
            publication_id=None,
            tags=feed_filter.publication_filter.tags,
            date_start=feed_filter.publication_filter.date_start,
            date_end=feed_filter.publication_filter.date_end
        )
    )
    
    result: FeedListDTO = FeedService().get_feeds(feed_filter)
    
    return FeedResponse(publications=result.publications)

@feed_router.get("/tags")
async def get_tags():
    ...

@feed_router.get("/search_publication/{public_filter}")
async def search(public_filter: PublicationFilter):
    ...

