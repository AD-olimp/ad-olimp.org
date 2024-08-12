from typing import Optional, Any

from sqlalchemy import Sequence, CursorResult

from src.database.session import get_session
from src.models.dto.schemas_get.dashboard import BoundaryData, PassingData
from src.models.dto.schemas_update.update_by_id import UpdateBoundaryDataScheme
from src.service.base import DataServiceInterface, AbstractModel
from src.repository import get_boundary_repository


class BoundaryService(DataServiceInterface):
    __slots__ = ('repo',)

    def __init__(self):
        self.repo = get_boundary_repository()

    async def get(self, data_id, session_getter=get_session) -> BoundaryData:
        async with session_getter() as session:
            data = await self.repo.get(ident=data_id, session=session)
        return BoundaryData.model_validate(data, from_attributes=True)

    async def get_many(self, data_filter, session_getter=get_session) -> list[BoundaryData]:
        async with session_getter() as session:
            return await self.repo.get_many(session=session, data_filter=data_filter)

    async def update(self, data_id, new_data: AbstractModel, session_getter=get_session) -> CursorResult[Any]:
        async with session_getter() as session:
            return await self.repo.update(session=session, ident=data_id, data=new_data)

    async def insert(self, data: BoundaryData, session_getter=get_session):
        async with session_getter() as session:
            return await self.repo.insert(session=session, data=data)
