from bson import ObjectId
from fastapi import APIRouter, Depends

from src.models import Publication
from src.api.v1.validation import check_publication_existence
from src.service import PublicationServiceInterface
from src.service.publication import get_publication_service


publication_router = APIRouter(
    prefix="/publications",
    tags=["Publication"]
)


@publication_router.post("/")
async def create_publication(publication: Publication, service=Depends(get_publication_service)):
    return str(await service.create_publication(publication))


@check_publication_existence
@publication_router.get("/{publication_id}/")
async def get_publication(
        publication_id: str,
        service: PublicationServiceInterface = Depends(get_publication_service)
) -> Publication:
    return await service.get_publication_by_id(publication_id=ObjectId(publication_id))


@check_publication_existence
@publication_router.post("/edit")
async def edit_publication(
        publication_id: str,
        new_publication: Publication,
        service: PublicationServiceInterface = Depends(get_publication_service)
):
    await service.update_publication(publication_id=ObjectId(publication_id), new_publication=new_publication)


@check_publication_existence
@publication_router.delete("/{publication_id}/")
async def delete_publication(
        publication_id: str,
        service: PublicationServiceInterface = Depends(get_publication_service)
):
    await service.delete_publication(publication_id=ObjectId(publication_id))
