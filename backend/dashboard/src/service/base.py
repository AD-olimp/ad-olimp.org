from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional


AbstractModel = TypeVar('AbstractModel')


class DataServiceInterface(ABC, Generic[AbstractModel]):
    """Интерфейс сервиса по работе с публикациями"""

    @abstractmethod
    async def create(self, data: AbstractModel):
        ...

    @abstractmethod
    async def get(self, data_id) -> Optional[AbstractModel]:
        ...

    @abstractmethod
    async def get_many(self, data_filter) -> list[Optional[AbstractModel]]:
        ...

    @abstractmethod
    async def update(self, data_id, new_data: AbstractModel):
        ...

    @abstractmethod
    async def delete(self, data_id):
        ...
