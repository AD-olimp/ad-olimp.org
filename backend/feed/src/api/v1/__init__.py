from fastapi import APIRouter

from .publication import publication_router
from .feed import feed_router

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(publication_router)
router_v1.include_router(feed_router)
