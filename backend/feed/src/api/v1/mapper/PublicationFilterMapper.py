from src.api.v1.schemas.feed import PublicationFilter
from src.models import PublicationFilterDTO


def to_domain(item: PublicationFilter) -> PublicationFilterDTO:
    return PublicationFilterDTO(
        publication_id=None,
        tags=item.publication_filter.tags,
        date_start=item.publication_filter.date_start,
        date_end=item.publication_filter.date_end
    )