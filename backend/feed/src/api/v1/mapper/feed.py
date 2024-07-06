from .protocol import BaseMapper

from src.api.v1.schemas.feed import FeedResponse, GetFeed, TagsScheme, TagsEnum, Publication
from src.models import FeedListDTO, GetFeedDTO, PublicationFilterDTO

from .publication import PublicationMapper

class GetFeedMapper(BaseMapper):
    @staticmethod
    def to_controller(item: FeedListDTO) -> list[Publication]:
        return [PublicationMapper.to_controller(public) for public in item.publications]
        
    @staticmethod
    def to_domain(item: GetFeed) -> GetFeedDTO:
        return GetFeedDTO(
            start=item.start,
            end=item.end,
            publication_filter=PublicationFilterDTO(
                publication_id=None,
                tags=item.publication_filter.tags,
                date_start=item.publication_filter.date_start,
                date_end=item.publication_filter.date_end
            )
        )
