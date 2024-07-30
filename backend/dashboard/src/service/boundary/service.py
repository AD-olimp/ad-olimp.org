from typing import Optional

from sqlalchemy import Sequence

from src.database.session import get_session
from src.models.dto.dashboard import BoundaryData
from src.service.base import DataServiceInterface, AbstractModel
from src.repository import get_boundary_repository
from result import Result


class BoundaryService(DataServiceInterface):
    def __init__(self):
        self.repo = get_boundary_repository()

    async def create(self, data: BoundaryData) -> Result:
        async with get_session() as session:
            return await self.repo.create(data=data, session=session)

    async def get(self, data_id) -> Result[Optional[AbstractModel]]:
        async with get_session() as session:
            return await self.repo.get(ident=data_id, session=session)

    async def get_many(self, data_filter) -> Sequence[Optional[AbstractModel]]:
        async with get_session() as session:
            return await self.repo.get_many(session=session, where_statement=data_filter)

    async def update(self, data_id, new_data: AbstractModel) -> Result:
        async with get_session() as session:
            return await self.repo.update(session=session, ident=data_id, data=new_data)

    async def delete(self, data_id) -> Result:
        async with get_session() as session:
            return await self.repo.delete(session=session, where_statement=data_id)