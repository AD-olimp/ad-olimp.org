from typing import Any

from sqlalchemy import CursorResult

from src.database.session import get_session
from src.models.dto.dashboard import DataFilter, OlympData
from src.repository import get_olymp_repository
from src.service.base import DataServiceInterface


class OlympDataService(DataServiceInterface):
    __slots__ = ('repo', )

    def __init__(self):
        self.repo = get_olymp_repository()

    async def get(self, data_id, session_getter=get_session) -> OlympData:
        async with session_getter() as session:
            data = await self.repo.get(ident=data_id, session=session)
        return OlympData.model_validate(data, from_attributes=True)

    async def get_many(self, data_filter: DataFilter, session_getter=get_session) -> list[OlympData]:
        async with session_getter() as session:
            return await self.repo.get_many(session=session, data_filter=data_filter)

    async def update(self, data_id, new_data) -> CursorResult[Any]:
        async with get_session() as session:
            return await self.repo.update(session=session, ident=data_id, data=new_data)

    async def insert(self, data: OlympData):
        async with get_session() as session:
            return await self.repo.insert(session=session, data=data)
