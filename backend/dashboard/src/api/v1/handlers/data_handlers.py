from fastapi import APIRouter, Depends

from src.models.dto.schemas_update.update_by_id import UpdateOlympDataScheme, UpdatePassingDataScheme, \
    UpdateBoundaryDataScheme
from src.service import get_passing_service, get_olymp_data_service, get_boundary_service, OlympDataService, \
    PassingService, BoundaryService

data_handler_router = APIRouter(
    prefix="/data",
    tags=["Data"]
)


@data_handler_router.get("/olymp/{data_id}")
async def get_olymp_data(
        data_id: int,
        service: OlympDataService = Depends(get_olymp_data_service)
):
    return await service.get(data_id=data_id)


@data_handler_router.get("/passing/{data_id}")
async def get_passing_data(
        data_id: int,
        service: PassingService = Depends(get_passing_service)
):
    return await service.get(data_id=data_id)


@data_handler_router.get("/boundary/{data_id}")
async def get_boundary_data(
        data_id: int,
        service: BoundaryService = Depends(get_boundary_service)
):
    return await service.get(data_id=data_id)


@data_handler_router.put("/olymp/{data_id}")
async def update_olymp_data(
        data_id: int,
        new_data: UpdateOlympDataScheme,
        service: OlympDataService = Depends(get_olymp_data_service)
):
    return await service.update(data_id=data_id, new_data=new_data)


@data_handler_router.put("/passing/{data_id}")
async def update_passing_data(
        data_id: int,
        new_data: UpdatePassingDataScheme,
        service: PassingService = Depends(get_passing_service)
):
    return await service.update(data_id=data_id, new_data=new_data)


@data_handler_router.put("/boundary/{data_id}")
async def update_boundary_data(
        data_id: int,
        new_data: UpdateBoundaryDataScheme,
        service: BoundaryService = Depends(get_boundary_service)
):
    return await service.update(data_id=data_id, new_data=new_data)


@data_handler_router.post("/olymp/")
async def insert_olymp_data(
        data: UpdateOlympDataScheme,
        service: OlympDataService = Depends(get_olymp_data_service)
):
    return await service.insert(data=data)


@data_handler_router.post("/passing/")
async def insert_passing_data(
        data: UpdatePassingDataScheme,
        service: PassingService = Depends(get_passing_service)
):
    return await service.insert(data=data)


@data_handler_router.post("/boundary/")
async def insert_boundary_data(
        data: UpdateBoundaryDataScheme,
        service: BoundaryService = Depends(get_boundary_service)
):
    return await service.insert(data=data)
