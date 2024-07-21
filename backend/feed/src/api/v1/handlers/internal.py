from bson import ObjectId
from fastapi import APIRouter, Depends


from src.models import Publication
from src.api.v1.validation import check_publication_existence
from src.service import PublicationServiceInterface
from src.service.publication import get_publication_service


internal_router = APIRouter(
    prefix="/internal",
    tags=["Internal"]
)


@internal_router.get("/ping", response_model=dict[str, str])
async def ping():
    return {"result": "pong"}


@internal_router.get("/mongodb/ping")
async def ping_mongodb():
    ...
