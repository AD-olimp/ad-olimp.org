from typing import Optional

from sqlalchemy import Sequence

from src.database.session import get_session
from src.models.dto.dashboard import BoundaryData
from src.service.base import DataServiceInterface, AbstractModel
from src.repository import get_boundary_repository
from result import Result


class BoundaryService(DataServiceInterface):
    __slots__ = ('repo',)

    def __init__(self):
        self.repo = get_boundary_repository()

    async def get(self, data_id) -> Result[Optional[AbstractModel]]:
        async with get_session() as session:
            return await self.repo.get(ident=data_id, session=session)

    async def get_many(self, data_filter) -> Sequence[Optional[AbstractModel]]:
        async with get_session() as session:
            return await self.repo.get_many(session=session, data_filter=data_filter)

    async def update(self, data_id, new_data: AbstractModel) -> Result:
        async with get_session() as session:
            return await self.repo.update(session=session, ident=data_id, data=new_data)
