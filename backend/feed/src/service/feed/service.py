from fastapi import Depends
from difflib import SequenceMatcher

from src.models.feeds import GetFeed
from .interface import FeedServiceInterface
from src.models.publication import Publication
from src.repository import RepositoryInterface, get_repository


class FeedService(FeedServiceInterface):
    """Сервис для работы с лентой постов"""
    
    confidence_interval = 0.8
    
    def __init__(self, Repo: RepositoryInterface = Depends(get_repository)):
        self.repo = Repo
