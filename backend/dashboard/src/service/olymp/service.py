from typing import Optional

from src.database.session import get_session
from src.models.dto.dashboard import OlympData
from src.repository import get_repository
from src.service.base import DataServiceInterface, AbstractModel

from result import Result


class OlympDataService(DataServiceInterface):
    __slots__ = ('repo', )

    def __init__(self):
        self.repo = get_repository()

    async def create(self, data: OlympData) -> Result:
        async with get_session() as session:
            return await self.repo.create(data=data, session=session)

    async def get(self, data_id) -> Result[Optional[AbstractModel]]:
        pass

    async def get_many(self, data_filter) -> list[Optional[AbstractModel]]:
        pass

    async def update(self, data_id, new_data: AbstractModel) -> Result:
        pass

    async def delete(self, data_id) -> Result:
        pass
