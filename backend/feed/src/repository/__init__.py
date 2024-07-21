from .mongo_repository import PublicationsMongoRepository
from .interface import RepositoryInterface
from src.database import AsyncMongoDB


def get_repository() -> PublicationsMongoRepository:
    return PublicationsMongoRepository(database=AsyncMongoDB.database)


__all__ = [
    'get_repository',
    'RepositoryInterface',
]
