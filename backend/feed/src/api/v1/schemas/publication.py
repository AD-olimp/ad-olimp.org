from enum import Enum
from pydantic import BaseModel

from src.common.models import TagsEnum
    

class Publication(BaseModel):
    title: str
    tags: list[TagsEnum]
    pictures_path: list[str]
    text: str
    