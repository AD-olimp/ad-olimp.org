from src.api.v1.schemas.publication import Publication
from src.models.publication import PublicationDTO


def to_controller(item: PublicationDTO) -> Publication:
    return Publication(
        title=item.title,
        tags=item.tags,
        pictures_path=item.pictures_path,
        text=item.text
    )
