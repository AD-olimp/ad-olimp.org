from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from . import config
from src.api.v1 import router_v1

"""
Запуск сервиса для работы с публикациями

команда запуска:

uvicorn app.main:forecast_service --reload --host 0.0.0.0 --port 8001
"""


forecast_service = FastAPI(
    title        = "ad-olimp.org publications",
    description  = "Сервис для работы с публикациями в ленту",
    version      = "1.0",
    root_path    = config.APP_NGINX_PREFIX
)


forecast_service.add_middleware(
    CORSMiddleware,
    allow_origins     = config.APP_CORS_ORIGINS_LIST,
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)

forecast_service.include_router(router_v1)

forecast_service.openapi_schema = get_openapi(
    title   = "iep-forecast-service",
    version = "1.0",
    routes  = forecast_service.routes,
    servers = [{'url': config.APP_NGINX_PREFIX}]
)
