from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI
from src.models.orm.passing import PassingPointORM
from src.models.dto.dashboard import DataFilter, PassingData


class PassingPointRepository(DataRepositoryI):
    async def get_many(
            self,
            session: AsyncSession,
            data_filter: DataFilter,
            limit: int = 100
    ) -> list[PassingData]:
        data = (await session.scalars(
            select(self.model)
            .where(and_(
                PassingPointORM.years.in_(data_filter.year),
                PassingPointORM.title.in_(data_filter.title),
                PassingPointORM.user_class.in_(data_filter.user_class)
            ))
            .limit(limit))).all()
        return [PassingData.model_validate(row, from_attributes=True) for row in data]
