from typing import Any
from bson import ObjectId
from abc import ABC, abstractmethod

from src.models import Publication


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
    async def get_all(self, session, publication_filters: dict[Any]) -> list[Publication]:
        ...

    @abstractmethod
    async def update(self, session, publication_id: ObjectId, new_publication: Publication) -> None:
        ...

    @abstractmethod
    async def delete(self, session, publication_id: ObjectId) -> None:
        ...
