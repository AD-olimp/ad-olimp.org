from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    id: int
    name: str
    # date: datetime
    text: str
    author: str
