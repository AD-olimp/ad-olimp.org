from fastapi import APIRouter

from .schemas.dashboard import (
    OlimpDataFilter,
    OlimpData,
    OlimpDataList,
    PassingData,
    PassingDataFilter,
    PassingDataList
)

dashboard_router = APIRouter(
    prefix="/data",
    tags=["Data"]
)


@dashboard_router.get("/search/{search_text}")
async def search(search_text):
    ...

@dashboard_router.get("/olimp/{data_filter}")
async def get_olymp_data_list(data_filter: OlimpDataFilter) -> OlimpDataList:
    ...

@dashboard_router.get("/olimp/{data_id}")
async def get_current_olimp_data(data_id: str) -> OlimpData:
    ...

@dashboard_router.get("/padding/{data_filter}")
async def get_current_passing_data(data_filter: PassingDataFilter) -> PassingDataList:
    ...

@dashboard_router.get("/padding/{data_id}")
async def get_current_passing_data(data_id: str) -> PassingData:
    ...
