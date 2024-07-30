from fastapi import APIRouter, Depends
from sqlalchemy import Sequence

from src.service import get_passing_service, get_olymp_data_service, get_boundary_service, OlympDataService, \
    PassingService, BoundaryService
from src.models.dto.dashboard import (
    OlympDataFilter,
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


@data_feed_handler_router.get("/olimp/{data_filter}/")
async def olymp_data_feed(
        data_filter: OlympDataFilter,
        service: OlympDataService = Depends(get_olymp_data_service)
) -> Sequence[AbstractModel | None]:
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)


@data_feed_handler_router.get("/passing/{data_filter}/")
async def passing_feed(
        data_filter: OlympDataFilter,
        service: PassingService = Depends(get_passing_service)
) -> list[OlympData]:
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)


@data_feed_handler_router.get("/olymp/{data_filter}/")
async def boundary_feed(
        data_filter: OlympDataFilter,
        service: BoundaryService = Depends(get_boundary_service)
) -> Sequence[AbstractModel | None]:
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)
