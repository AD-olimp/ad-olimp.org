from typing import Optional, Any

from sqlalchemy import Sequence, CursorResult

from src.database.session import get_session
from src.models import PassingData
from src.repository import get_passing_repository
from src.service.base import DataServiceInterface, AbstractModel


class PassingService(DataServiceInterface):
    __slots__ = ('repo',)

    def __init__(self):
        self.repo = get_passing_repository()

    async def get(self, data_id, session_getter=get_session) -> PassingData:
        async with session_getter() as session:
            data = await self.repo.get(ident=data_id, session=session)
        return PassingData.model_validate(data, from_attributes=True)

    async def get_many(self, data_filter) -> list[PassingData]:
        async with get_session() as session:
            return await self.repo.get_many(session=session, data_filter=data_filter)

    async def update(self, data_id, new_data: AbstractModel) -> CursorResult[Any]:
        async with get_session() as session:
            return await self.repo.update(session=session, ident=data_id, data=new_data)

    async def insert(self, data: PassingData):
        async with get_session() as session:
            return await self.repo.insert(session=session, data=data)
