from fastapi import APIRouter

from src.api.v1.handlers.data_feed_handlers import data_feed_handler_router
from src.api.v1.handlers.data_handlers import data_handler_router


router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(data_handler_router)
router_v1.include_router(data_feed_handler_router)
