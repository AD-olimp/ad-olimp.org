from typing import Any
from bson import ObjectId
from abc import ABC, abstractmethod

from src.models import Publication, GetFeed, PublicationSearch, PublicationFilter
from src.models.feeds import GetSearch


class RepositoryInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""

    __slots__ = ('collection', )

    @abstractmethod
    async def add(self, session, new_publication: Publication) -> None:
        ...

    @abstractmethod
    async def get(self, session, publication_filter: dict[Any]) -> Publication:
        ...

    @abstractmethod
    async def get_by_filter(self, session, publication_filters: GetFeed) -> list[Publication]:
        ...

    @abstractmethod
    async def search_by_text(self, session, search_filter: GetSearch) -> list[Publication]:
        ...

    @abstractmethod
    async def update(self, session, publication_id: ObjectId, new_publication: Publication) -> None:
        ...

    @abstractmethod
    async def delete(self, session, publication_id: ObjectId) -> None:
        ...
