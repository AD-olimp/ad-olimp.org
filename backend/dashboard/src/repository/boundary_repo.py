from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI, AbstractModel
from ..models.orm.boundary import BoundaryPointORM


class BoundaryPointRepository(DataRepositoryI):
    async def create(self, data: AbstractModel, session: AsyncSession):
        session.add(BoundaryPointORM())
