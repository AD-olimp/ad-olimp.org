from pymongo import MongoClient
from typing import List, Dict, Any


def get_repository() -> MongoRepository:
    client = MongoClient("mongodb://localhost:27017")
    
    return MongoRepository(client, "mydatabase", "mycollection")