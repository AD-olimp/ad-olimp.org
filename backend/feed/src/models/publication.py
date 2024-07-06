from dataclasses import dataclass

from src.common.models import TagsEnum


@dataclass
class PublicationDTO:
    publication_id: str
    title: str
    tags: list[TagsEnum]
    pictures_path: list[str]
    text: str


@dataclass
class FeedListDTO:
    publications: list[PublicationDTO]