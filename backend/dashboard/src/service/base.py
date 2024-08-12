from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

from src.models.dto.schemas_get.dashboard import DataFilter

AbstractModel = TypeVar('AbstractModel')


class DataServiceInterface(ABC, Generic[AbstractModel]):
    """Интерфейс сервиса по работе с публикациями"""

    async def create(self, data: AbstractModel):
        ...

    @abstractmethod
    async def get(self, data_id, session_getter) -> Optional[AbstractModel]:
        ...

    @abstractmethod
    async def get_many(self, data_filter: DataFilter) -> list[Optional[AbstractModel]]:
        ...

    @abstractmethod
    async def update(self, data_id, new_data: AbstractModel):
        ...

    async def delete(self, data_id):
        ...
