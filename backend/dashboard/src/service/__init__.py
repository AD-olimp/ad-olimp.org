from .olymp.service import OlympDataService
from .boundary.service import BoundaryService
from .passing.service import PassingService


def get_olymp_data_service():
    return OlympDataService()


def get_boundary_service():
    return BoundaryService()


def get_passing_service():
    return PassingService()


__all__ = [
    'get_olymp_data_service', 'get_boundary_service', 'get_passing_service',
    'OlympDataService', 'BoundaryService', 'PassingService'
]
