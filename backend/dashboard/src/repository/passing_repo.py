from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI, AbstractModel
from ..models.orm.passing import PassingPointORM


class PassingPointRepository(DataRepositoryI):
    async def create(self, data: AbstractModel, session: AsyncSession):
        session.add(PassingPointORM())
        