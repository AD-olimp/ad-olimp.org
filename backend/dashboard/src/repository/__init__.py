from .interface import DataRepositoryI
from .olymp_repo import OlympRepository

from src.models.orm import OlympORM, BoundaryPointORM, PassingPointORM


def get_olymp_repository() -> DataRepositoryI:
    return OlympRepository(model=OlympORM)


def get_passing_repository() -> DataRepositoryI:
    return DataRepositoryI(model=PassingPointORM)


def get_boundary_repository() -> DataRepositoryI:
    return DataRepositoryI(model=BoundaryPointORM)


__all__ = [
    'get_olymp_repository',
    'get_passing_repository',
    'get_boundary_repository',
    'DataRepositoryI',
]
