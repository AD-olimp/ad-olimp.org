from fastapi import APIRouter, Depends

from src.models.dto.dashboard import OlympData, PassingData, BoundaryData
from src.service import get_passing_service, get_olymp_data_service, get_boundary_service

data_handler_router = APIRouter(
    prefix="/data",
    tags=["Data"]
)


@data_handler_router.get("/olymp/{data_id}")
async def get_olymp_data(data_id: str, service=Depends(get_olymp_data_service)) -> OlympData:
    return service.get(data_id=data_id)


@data_handler_router.get("/passing/{data_id}")
async def get_passing_data(data_id: str, service=Depends(get_passing_service)) -> PassingData:
    ...


@data_handler_router.get("/boundary/{data_id}")
async def get_boundary_data(data_id: str, service=Depends(get_boundary_service)) -> BoundaryData:
    ...
