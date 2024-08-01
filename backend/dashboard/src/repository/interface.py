from abc import ABC, abstractmethod
from typing import TypeVar, Tuple, Any

from result import Result
from sqlalchemy import select, Sequence, delete, Row, RowMapping, ScalarResult, update, bindparam
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.orm.base import BaseTable

AbstractModel = TypeVar('AbstractModel')


class DataRepositoryI(ABC):
    """Интерфейс репозитория по работе с публикациями"""

    session: AsyncSession

    __slots__ = ('session', 'model',)

    def __init__(self, model):
        self.model = model

    async def get(self, ident, session: AsyncSession) -> AbstractModel:
        return await session.get(entity=self.model, ident=ident)

    @abstractmethod
    async def get_many(
            self,
            session: AsyncSession,
            data_filter,
            limit: int = 100) -> Sequence[Row[Any] | RowMapping | Any]:
        ...

    async def update(
            self,
            session: AsyncSession,
            ident,
            data: AbstractModel
    ) -> ScalarResult[Any]:
        return (await session.scalars(
            update(self.model)
            .where(self.model.c.id == bindparam(ident))
            .values(
                **data.dict()
            )
        ))
