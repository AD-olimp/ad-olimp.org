from fastapi import APIRouter, Depends

from .schemas.feed import PublicationSearch, GetFeed, Publication, TagsScheme
from .mapper.feed import GetFeedMapper

from src.service.feed.service import FeedService
from src.database.mongodb import get_repository


feed_router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)


@feed_router.get("/tags")
async def get_tags() -> TagsScheme:
    return TagsScheme()


@feed_router.post("/feed", response_model=list[Publication])
async def get_feed(feed_filter: GetFeed, Repo = Depends(get_repository)) -> list[Publication]:
    
    return GetFeedMapper.to_controller(
        FeedService(Repo).get_feeds(
            feed_filter=GetFeedMapper.to_domain(feed_filter)
        )
    )


@feed_router.post("/search_publication", response_model=list[Publication])
async def search(search: PublicationSearch, Repo = Depends(get_repository)) -> list[Publication]:
        
    return GetFeedMapper.to_controller(
        FeedService(Repo).search_feeds(
            feed_filter=GetFeedMapper.to_domain(search.publication_filter),
            search_text=search.text
        )
    )
