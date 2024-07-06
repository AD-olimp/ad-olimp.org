from .protocol import BaseMapper

from src.api.v1.schemas.publication import Publication, TagsEnum
from src.service.models import PublicationDTO



class PublicationMapper(BaseMapper):
    @classmethod
    def to_controller(cls, item: PublicationDTO) -> Publication:
        return Publication(
            title=item.title,
            tags=item.tags,
            pictures_path=item.pictures_path,
            text=item.text
        )