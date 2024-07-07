from src.api.v1.mapper import PublicationMapper, PublicationFilterMapper

from src.api.v1.schemas.feed import Publication, GetFeed
from src.models import FeedListDTO, GetFeedDTO


def to_controller(item: FeedListDTO) -> list[Publication]:
    return [PublicationMapper.to_controller(public) for public in item.publications]


def to_domain(item: GetFeed) -> GetFeedDTO:
    return GetFeedDTO(
        start=item.start,
        end=item.end,
        publication_filter=PublicationFilterMapper.to_domain(item.publication_filter)
    )
