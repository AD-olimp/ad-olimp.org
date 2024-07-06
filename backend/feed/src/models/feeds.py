from typing import Optional
from dataclasses import dataclass
from src.common.models import TagsEnum


@dataclass
class PublicationFilterDTO:
    publication_id: Optional[str]
    tags: Optional[list[TagsEnum]]
    date_start: Optional[str]
    date_end: Optional[str]


@dataclass
class GetFeedDTO:
    publication_filter: PublicationFilterDTO
    start: int 
    end: int
