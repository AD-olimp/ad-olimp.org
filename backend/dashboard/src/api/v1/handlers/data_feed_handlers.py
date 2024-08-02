from fastapi import APIRouter, Depends
from sqlalchemy import Sequence

from src.service import get_passing_service, get_olymp_data_service, get_boundary_service, OlympDataService, \
    PassingService, BoundaryService
from src.models.dto.dashboard import (
    DataFilter,
    OlympData
)
from src.service.base import AbstractModel

data_feed_handler_router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)


@data_feed_handler_router.get("/search/{search_text}/")
async def search(search_text, service=Depends()):
    ...


@data_feed_handler_router.get("/olimp/")
async def olymp_data_feed(
        data_filter: DataFilter,
        service: OlympDataService = Depends(get_olymp_data_service)
):  # -> Sequence[AbstractModel | None]:
    return await service.get_many(data_filter=data_filter)


@data_feed_handler_router.get("/passing/")
async def passing_feed(
        data_filter: DataFilter,
        service: PassingService = Depends(get_passing_service)
):  # -> Sequence[AbstractModel | None]:
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)


@data_feed_handler_router.get("/olymp/")
async def boundary_feed(
        data_filter: DataFilter,
        service: BoundaryService = Depends(get_boundary_service)
):  # -> Sequence[AbstractModel | None]:
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)
