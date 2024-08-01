from typing import Any

from sqlalchemy import Sequence, select, and_, update, bindparam, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI, AbstractModel
from src.models.orm.olymp import OlympORM
from src.models.dto.dashboard import DataFilter


class OlympRepository(DataRepositoryI):
    async def get_many(
            self,
            session: AsyncSession,
            data_filter: DataFilter,
            limit: int = 100):
        return (await session.scalars(
                 select(self.model)
                .where(and_(
                    OlympORM.title.in_(data_filter.title),
                    OlympORM.user_class.in_(data_filter.user_class)
                ))
                .limit(limit))).all()
