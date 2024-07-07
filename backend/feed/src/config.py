import os
from dotenv import load_dotenv
from dataclasses import dataclass, field

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


@dataclass
class NGINXConfig:
    APP_PREFIX: str = os.getenv("APP_NGINX_PREFIX")


@dataclass
class MongoDBConfig:
    host: str = os.getenv("MONGODB_HOST")
    port: str = os.getenv("MONGODB_PORT")
    database: str = os.getenv("DATABASE")
    collection: str = os.getenv("collection")
    url: str = field(init=False)
    
    def __post_init__(self):
        self.url = f"mongodb://{self.host}:{self.port}"
