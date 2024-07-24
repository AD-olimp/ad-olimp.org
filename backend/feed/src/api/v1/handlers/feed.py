from fastapi import APIRouter, Depends

from src.models import PublicationSearch, Publication, TagsScheme, PublicationFilter, GetFeed
from src.models.feeds import GetSearch

from src.service.feed import get_feed_service
from src.service.feed.interface import FeedServiceInterface

feed_router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)

# закомментил, потому что полностью заменяется хендлером search
# @feed_router.post(path="/", response_model=list[Publication])
# async def get_feed_handler(
#         get_feed: GetFeed,
#         service: FeedServiceInterface = Depends(get_feed_service)
# ) -> list[Publication]:
#     return await service.get_feeds(feeds_filter=get_feed)


@feed_router.get("/tags")
async def get_tags_handler() -> TagsScheme:
    return TagsScheme()


@feed_router.post(path="/search", response_model=list[Publication])
async def search_handler(
        search: GetSearch,
        service: FeedServiceInterface = Depends(get_feed_service)
) -> list[Publication]:
    return await service.get_search(search_filter=search)
