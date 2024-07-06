from fastapi import APIRouter

from .dashboard import dashboard_router
from .forecast import forecast_router

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(dashboard_router)
router_v1.include_router(forecast_router)
