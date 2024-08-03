from fastapi import APIRouter, Depends

from src.service import get_passing_service, get_olymp_data_service, get_boundary_service, OlympDataService, \
    PassingService, BoundaryService
from src.models.dto.schemas_get.dashboard import (
    DataFilter
)

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
):
    return await service.get_many(data_filter=data_filter)


@data_feed_handler_router.get("/passing/")
async def passing_feed(
        data_filter: DataFilter,
        service: PassingService = Depends(get_passing_service)
):
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)


@data_feed_handler_router.get("/olymp/")
async def boundary_feed(
        data_filter: DataFilter,
        service: BoundaryService = Depends(get_boundary_service)
):
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)
