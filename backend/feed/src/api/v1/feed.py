from fastapi import APIRouter, Depends

from .schemas.feed import PublicationSearch, Publication, TagsScheme, PublicationFilter
from .mapper import GetFeedMapper, PublicationFilterMapper

from src.service.feed.service import FeedService
from src.database.uow import get_uow


feed_router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)


@feed_router.post(path="/", response_model=list[Publication])
async def get_feed_handler(
        start: int,
        end: int,
        publication_filter: PublicationFilter,
        UoW=Depends(get_uow)
) -> list[Publication]:

    return GetFeedMapper.to_controller(
        FeedService(UoW).get_feeds(
            feed_filter=GetFeedMapper.to_domain(start, end, publication_filter)
        )
    )


@feed_router.get("/tags")
async def get_tags_handler() -> TagsScheme:
    return TagsScheme()


@feed_router.post(path="/search", response_model=list[Publication])
async def search_handler(search: PublicationSearch, UoW=Depends(get_uow)) -> list[Publication]:
        
    return GetFeedMapper.to_controller(
        FeedService(UoW).search_feeds(
            feed_filter=PublicationFilterMapper.to_domain(search.publication_filter),
            search_text=search.text
        )
    )
