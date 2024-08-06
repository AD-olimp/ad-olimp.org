from sqlalchemy import select, and_, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI
from src.models.dto.schemas_get.dashboard import DataFilter, BoundaryData
from src.models.orm.boundary import BoundaryPointORM


class BoundaryPointRepository(DataRepositoryI):
    async def get_many(
            self,
            session: AsyncSession,
            data_filter: DataFilter,
            limit: int = 100) -> list[BoundaryData]:
        data = (await session.scalars(
                 select(self.model)
                .where(and_(
                    BoundaryPointORM.title.in_(data_filter.title),
                    BoundaryPointORM.user_class.in_(data_filter.user_class),
                    BoundaryPointORM.years.in_(data_filter.year)
                ))
                .limit(limit))).all()
        return [BoundaryData.model_validate(row, from_attributes=True) for row in data]
