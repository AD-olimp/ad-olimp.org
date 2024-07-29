from sqlalchemy.ext.asyncio import AsyncSession

from .interface import DataRepositoryI, AbstractModel
from ..models.orm.olymp import OlympORM


class OlympRepository(DataRepositoryI):
    async def create(self, data: AbstractModel, session: AsyncSession):
        session.add(OlympORM())
