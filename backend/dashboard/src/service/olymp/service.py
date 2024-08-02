from typing import Optional, Any

from sqlalchemy import Sequence, ScalarResult

from src.database.session import get_session
from src.models.dto.dashboard import OlympData, DataFilter, OlympDataORM
from src.repository import get_olymp_repository
from src.service.base import DataServiceInterface, AbstractModel

from result import Result


class OlympDataService(DataServiceInterface):
    __slots__ = ('repo', )

    def __init__(self):
        self.repo = get_olymp_repository()

    async def get(self, data_id):
        async with get_session() as session:
            return await self.repo.get(ident=data_id, session=session)

    async def get_many(self, data_filter: DataFilter) -> Sequence[Optional[AbstractModel]]:
        async with get_session() as session:
            return await self.repo.get_many(session=session, data_filter=data_filter)

    async def update(self, data_id, new_data: OlympDataORM) -> ScalarResult[Any]:
        async with get_session() as session:
            return await self.repo.update(session=session, ident=data_id, data=new_data)
