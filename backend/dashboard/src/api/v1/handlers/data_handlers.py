from typing import Any, Coroutine

from fastapi import APIRouter, Depends
from result import Ok, Err
from sqlalchemy import ScalarResult

from src.models.dto.dashboard import OlympData, PassingData, BoundaryData
from src.models.orm import BoundaryPointORM, OlympORM, PassingPointORM
from src.service import get_passing_service, get_olymp_data_service, get_boundary_service, OlympDataService, \
    PassingService, BoundaryService
from src.service.base import AbstractModel

data_handler_router = APIRouter(
    prefix="/data",
    tags=["Data"]
)


@data_handler_router.get("/olymp/{data_id}")
async def get_olymp_data(
        data_id: str,
        service: OlympDataService = Depends(get_olymp_data_service)
) -> Ok[Any | None] | Err[Any]:
    return await service.get(data_id=data_id)


@data_handler_router.get("/passing/{data_id}")
async def get_passing_data(
        data_id: str,
        service: PassingService = Depends(get_passing_service)
) -> Ok[Any | None] | Err[Any]:
    return await service.get(data_id=data_id)


@data_handler_router.get("/boundary/{data_id}")
async def get_boundary_data(
        data_id: str,
        service: BoundaryService = Depends(get_boundary_service)
) -> Ok[Any | None] | Err[Any]:
    return await service.get(data_id=data_id)


@data_handler_router.get("/olymp/{data_id}")
async def update_olymp_data(
        data_id: str,
        new_data: OlympORM,
        service: OlympDataService = Depends(get_olymp_data_service)
) -> ScalarResult[Any]:
    return await service.update(data_id=data_id, new_data=new_data)


@data_handler_router.get("/passing/{data_id}")
async def update_passing_data(
        data_id: str,
        new_data: PassingPointORM,
        service: PassingService = Depends(get_passing_service)
) -> ScalarResult[Any]:
    return await service.update(data_id=data_id, new_data=new_data)


@data_handler_router.get("/boundary/{data_id}")
async def update_boundary_data(
        data_id: str,
        new_data: BoundaryPointORM,
        service: BoundaryService = Depends(get_boundary_service)
) -> ScalarResult[Any]:
    return await service.update(data_id=data_id, new_data=new_data)