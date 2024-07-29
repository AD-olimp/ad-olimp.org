from fastapi import APIRouter, Depends

from src.models.dto.dashboard import (
    OlympDataFilter,
    OlympData
)

data_feed_handler_router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)




@data_feed_handler_router.get("/search/{search_text}/")
async def search(search_text, service=Depends()):
    ...


@data_feed_handler_router.get("/olimp/{data_filter}/")
async def olymp_data_feed(data_filter: OlympDataFilter) -> list[OlympData]:
    """Получить список олимпиад """
    ...

@data_feed_handler_router.get("/passing/{data_filter}/")
async def passing_feed(data_filter: OlympDataFilter) -> list[OlympData]:
    """Получить список олимпиад """
    ...

@data_feed_handler_router.get("/olymp/{data_filter}/")
async def boundary_feed(data_filter: OlympDataFilter) -> list[OlympData]:
    """Получить список олимпиад """
    ...
