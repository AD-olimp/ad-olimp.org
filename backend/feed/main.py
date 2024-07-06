from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from . import config
from src.api.v1 import router_v1

"""
Запуск сервиса для работы с публикациями

команда запуска:

uvicorn main:feed_service --reload --host 0.0.0.0 --port 8000
"""


feed_service = FastAPI(
    title        = "ad-olimp.org publications",
    description  = "Сервис для работы с публикациями в ленту",
    version      = "1.0",
    root_path    = config.APP_NGINX_PREFIX
)


feed_service.add_middleware(
    CORSMiddleware,
    allow_origins     = ["*"],
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)

feed_service.include_router(router_v1)
