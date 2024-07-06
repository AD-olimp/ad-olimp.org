from enum import Enum
from pydantic import BaseModel

from .publication import Publication
from src.common.models import TagsEnum
    

class FeedResponse(BaseModel):
    publications: list[Publication]


class PublicationFilter(BaseModel):
    tags: list[TagsEnum]
    date_start: str
    date_end: str


class GetFeed(BaseModel):
    publication_filter: PublicationFilter
    start: int 
    end: int