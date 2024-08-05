from .boundary_repo import BoundaryPointRepository
from .interface import DataRepositoryI
from .olymp_repo import OlympRepository

from src.models.orm import OlympORM, BoundaryPointORM, PassingPointORM
from .passing_repo import PassingPointRepository


def get_olymp_repository() -> OlympRepository:
    return OlympRepository(model=OlympORM)


def get_passing_repository() -> PassingPointRepository:
    return PassingPointRepository(model=PassingPointORM)


def get_boundary_repository() -> BoundaryPointRepository:
    return BoundaryPointRepository(model=BoundaryPointORM)


__all__ = [
    'get_olymp_repository',
    'get_passing_repository',
    'get_boundary_repository',
    'DataRepositoryI',
]
