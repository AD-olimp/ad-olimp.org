from .service import PublicationService
from .interface import PublicationServiceInterface


def get_publication_service() -> PublicationService:
    return PublicationService()


__all__ = ['get_publication_service', 'PublicationServiceInterface']
