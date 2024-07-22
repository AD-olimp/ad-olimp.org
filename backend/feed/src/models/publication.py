from pydantic import BaseModel
from enum import Enum


class TagsEnum(str, Enum):
    economics = 'Экономика'
    informatics = 'Информатика'
    admission = 'Поступление'
    vseros = 'Всерос'
    moscow = 'Сборная москвы'
    education = 'Образование'


class Publication(BaseModel):
    title: str
    tags: list[TagsEnum]
    pictures_path: list[str]
    text: str
    data: str


class PublicationFilter(BaseModel):
    tags: list[TagsEnum]
    date_start: str
    date_end: str


class PublicationSearch(BaseModel):
    publication_filter: PublicationFilter
    text: str
