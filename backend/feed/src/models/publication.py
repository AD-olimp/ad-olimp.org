from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class VariablesEnum(str, Enum):
    title = "title"
    text = "text"


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
    data: datetime


class PublicationFilter(BaseModel):
    tags: list[TagsEnum]
    date_start: datetime
    date_end: datetime


class PublicationSearch(BaseModel):
    publication_filter: PublicationFilter
    text: str
