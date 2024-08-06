from fastapi import APIRouter, Depends

from src.service import get_passing_service, get_olymp_data_service, get_boundary_service, OlympDataService, \
    PassingService, BoundaryService
from src.models.dto.schemas_get.dashboard import (
    DataFilter, OlympData, PassingData, BoundaryData
)

data_feed_handler_router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)


@data_feed_handler_router.get("/search/{search_text}/")
async def search(search_text, service=Depends()):
    ...


@data_feed_handler_router.post("/olymp/", response_model=list[OlympData])
async def olymp_data_feed(
        data_filter: DataFilter,
        service: OlympDataService = Depends(get_olymp_data_service)
) -> list[OlympData]:
    return await service.get_many(data_filter=data_filter)


@data_feed_handler_router.post("/passing/", response_model=list[PassingData])
async def passing_feed(
        data_filter: DataFilter,
        service: PassingService = Depends(get_passing_service)
) -> list[PassingData]:
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)


@data_feed_handler_router.post("/boundary/", response_model=list[BoundaryData])
async def boundary_feed(
        data_filter: DataFilter,
        service: BoundaryService = Depends(get_boundary_service)
) -> list[BoundaryData]:
    """Получить список олимпиад """
    return await service.get_many(data_filter=data_filter)
