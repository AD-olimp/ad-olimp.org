from .mongo_repository import MongoRepositoryPublications
from .interface import RepositoryInterface


def get_repository(collection):
    return MongoRepositoryPublications(collection)


__all__ = [
    'MongoRepositoryPublications',
    'RepositoryInterface',
    'get_repository'
]
