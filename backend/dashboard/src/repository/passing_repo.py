from sqlalchemy import Sequence, select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI, AbstractModel
from src.models.orm.passing import PassingPointORM
from ..models.dto.dashboard import DataFilter
from ..models.orm.base import BaseTable


class PassingPointRepository(DataRepositoryI):
    async def get_many(
            self,
            session: AsyncSession,
            data_filter: DataFilter,
            limit: int = 100):
        return (await session.scalars(
            select(self.model)
            .where(and_(
                PassingPointORM.years.in_(data_filter.year),
                PassingPointORM.title.in_(data_filter.title),
                PassingPointORM.user_class.in_(data_filter.user_class)
            ))
            .limit(limit))).all()

    async def update(self, session, ident, data: AbstractModel):
        pass
        