from typing import Optional

from sqlalchemy import Sequence, Result

from src.database.session import get_session
from src.models.dto.dashboard import DataFilter
from src.repository import get_passing_repository
from src.service.base import DataServiceInterface, AbstractModel


class PassingService(DataServiceInterface):
    __slots__ = ('repo',)

    def __init__(self):
        self.repo = get_passing_repository()

    async def get(self, data_id):
        async with get_session() as session:
            return await self.repo.get(ident=data_id, session=session)

    async def get_many(self, data_filter) -> Sequence[Optional[AbstractModel]]:
        async with get_session() as session:
            return await self.repo.get_many(session=session, data_filter=data_filter)

    async def update(self, data_id, new_data: AbstractModel) -> Result:
        async with get_session() as session:
            return await self.repo.update(session=session, ident=data_id, data=new_data)
