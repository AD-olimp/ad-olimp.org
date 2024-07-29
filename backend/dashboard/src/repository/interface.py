from abc import ABC, abstractmethod
from typing import TypeVar

from result import Result
from sqlalchemy import select, Sequence, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.orm.base import BaseTable

AbstractModel = TypeVar('AbstractModel')


class DataRepositoryI(ABC):
    """Интерфейс репозитория по работе с публикациями"""

    session: AsyncSession

    __slots__ = ('session', 'model', )

    def __init__(self, model):
        self.model = model

    @abstractmethod
    async def create(self, data: AbstractModel, session: AsyncSession) -> Result:
        ...

    async def get(self, ident, session: AsyncSession) -> AbstractModel:
        return await session.get(entity=self.model, ident=ident)

    async def get_by_where(self, where_statement, session: AsyncSession) -> list[AbstractModel]:
        return (
            await session.execute(
                select(self.model)
                .where(where_statement)
            )
        ).one_or_none()

    async def get_many(
            self,
            session: AsyncSession,
            where_statement,
        limit: int = 100) -> Sequence[BaseTable]:

        return (
            await session.scalars(
                select(self.model)
                .where(where_statement)
                .limit(limit)
            )
        ).all()

    async def delete(self, where_statement, session: AsyncSession) -> Result:
        await session.execute(
            delete(self.model)\
            .where(where_statement)
        )
