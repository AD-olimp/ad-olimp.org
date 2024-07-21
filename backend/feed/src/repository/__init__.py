from .mongo_repository import PublicationsMongoRepository
from .interface import RepositoryInterface


def get_repository() -> PublicationsMongoRepository:
    # return PublicationsMongoRepository(database=AsyncMongoDB.database)
    return PublicationsMongoRepository()


__all__ = [
    'get_repository',
    'RepositoryInterface',
]
