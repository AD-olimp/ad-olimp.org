from enum import Enum
from pydantic import BaseModel, Field

from .publication import Publication
from src.common.models import TagsEnum
    

class FeedResponse(BaseModel):
    publications: list[Publication]


class PublicationFilter(BaseModel):
    tags: list[TagsEnum]
    date_start: str
    date_end: str


class PublicationSearch(BaseModel):
    publication_filter: PublicationFilter
    text: str
    

class GetFeed(BaseModel):
    publication_filter: PublicationFilter
    start: int 
    end: int


class TagsScheme(BaseModel):
    tags: tuple[TagsEnum] = Field(
        default = tuple(TagsEnum.__dict__['_value2member_map_'].keys())
    )
