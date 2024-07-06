from pymongo import MongoClient
from typing import List, Dict, Any

from src.repository.mongo_repository import MongoRepositoryPublications
from src.repository.interface import RepositoryInterface
from src.config import MongoDBConfig


def get_repository() -> RepositoryInterface:
    client = MongoClient(MongoDBConfig.url)
    
    return MongoRepositoryPublications(client, MongoDBConfig.database, MongoDBConfig.collection)
