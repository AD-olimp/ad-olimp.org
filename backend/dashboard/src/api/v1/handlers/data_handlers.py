from fastapi import APIRouter, Depends

from src.models.dto.dashboard import OlympData, PassingData, BoundaryData


data_handler_router = APIRouter(
    prefix="/data",
    tags=["Data"]
)


@data_handler_router.get("/olymp/{data_id}")
async def get_olymp_data(data_id: str, service=Depends(get_service)) -> OlympData:
    ...


@data_handler_router.get("/passing/{data_id}")
async def get_passing_data(data_id: str) -> PassingData:
    ...


@data_handler_router.get("/boundary/{data_id}")
async def get_boundary_data(data_id: str) -> BoundaryData:
    ...
