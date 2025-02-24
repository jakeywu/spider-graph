from fastapi import APIRouter
from app.src.utils.output import api_output


pcc_router = APIRouter()


@pcc_router.get("/api/spider-net/health/check")
async def health_check():
    """
    health check
    :return:
    """
    return api_output()
