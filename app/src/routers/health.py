from fastapi import APIRouter
from src.utils.output import api_output


HEALTH_ROUTER = APIRouter()


@HEALTH_ROUTER.get("/api/health/check/status")
async def health_check():
    """
    health check
    :return:
    """
    return api_output()
