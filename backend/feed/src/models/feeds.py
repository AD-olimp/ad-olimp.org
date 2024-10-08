from pydantic import BaseModel, Field

from .publication import PublicationFilter, TagsEnum, PublicationSearch, VariablesEnum


class GetFeed(BaseModel):
    publication_filter: PublicationFilter
    start: int
    end: int


class GetSearch(BaseModel):
    search_filter: PublicationSearch
    start: int
    end: int


class TagsScheme(BaseModel):
    tags: tuple[TagsEnum] = Field(
        default=tuple(TagsEnum.__dict__['_value2member_map_'].keys())
    )
