from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI
from src.models.orm.olymp import OlympORM
from src.models.dto.dashboard import DataFilter, OlympData


class OlympRepository(DataRepositoryI):
    async def get_many(
            self,
            session: AsyncSession,
            data_filter: DataFilter,
            limit: int = 100
    ) -> list[OlympData]:
        data = (await session.scalars(
                 select(self.model)
                .where(and_(
                    OlympORM.title.in_(data_filter.title),
                    OlympORM.user_class.in_(data_filter.user_class)
                ))
                .limit(limit))).all()
        return [OlympData.model_validate(row, from_attributes=True) for row in data]
