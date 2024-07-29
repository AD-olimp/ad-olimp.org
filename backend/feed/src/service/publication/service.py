from bson import ObjectId
from datetime import date
from fastapi import Depends

from src.database import get_db
from src.models import Publication
from src.repository import get_repository
from src.repository import RepositoryInterface
from .interface import PublicationServiceInterface


class PublicationService(PublicationServiceInterface):
    """Сервис для работы с постами"""

    def __init__(self):
        self.repo: RepositoryInterface = get_repository()

    async def create_publication(
            self,
            publication: Publication,
            session=Depends(get_db)
    ) -> None:

        async with get_db() as session:
            return await self.repo.add(session=session, new_publication=publication)

    async def get_publication_by_id(self, publication_id: ObjectId):
        async with get_db() as session:
            return await self.repo.get(session=session, publication_filter={"_id": publication_id})

    async def get_publication_by_date(self, public_date: date):
        async with get_db() as session:
            return await self.repo.get(session=session, publication_filter={"date": public_date})

    async def update_publication_field(self, publication_id: ObjectId, field, new_value):
        async with get_db() as session:
            # Получаем публикацию по id
            publication: Publication = await self.repo.get(
                session=session,
                publication_filter={"_id": publication_id}
            )

            # Устанавливаем новое значение в поле
            publication.__setattr__(field, new_value)

            # обновляем
            await self.repo.update(session=session, publication_id=publication_id, new_publication=publication)

    async def update_publication(self, publication_id: ObjectId, new_publication: Publication):
        async with get_db() as session:
            await self.repo.update(
                session=session,
                publication_id=publication_id,
                new_publication=new_publication
            )

    async def delete_publication(self, publication_id: ObjectId):
        async with get_db() as session:
            return await self.repo.delete(session=session, publication_id=publication_id)
