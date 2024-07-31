from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI, AbstractModel
from src.models.dto.dashboard import DataFilter
from src.models.orm.boundary import BoundaryPointORM


class BoundaryPointRepository(DataRepositoryI):
    async def update(self, session, ident, data: AbstractModel):
        ...

    async def get(self, session: AsyncSession, data_filter):
        ...

    async def get_many(
            self,
            session: AsyncSession,
            data_filter: DataFilter,
            limit: int = 100) -> None:
        return (await session.scalars(
                 select(self.model)
                .where(and_(
                    BoundaryPointORM.title.in_(data_filter.title),
                    BoundaryPointORM.user_class.in_(data_filter.user_class),
                    BoundaryPointORM.years.in_(data_filter.year)
                ))
                .limit(limit))).all()
