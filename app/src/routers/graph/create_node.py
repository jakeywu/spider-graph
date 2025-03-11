from fastapi import APIRouter
from datetime import datetime, UTC
from pydantic import BaseModel, Field
from typing import Optional
import uuid
from src.schemas.graph import CreateNodeRequest, CreateNodeResponse

class APIOutputResponse(BaseModel):
    code: int = Field(200, description="API状态码")
    message: str = Field("success", description="API响应消息")
    data: Optional[CreateNodeResponse] = Field(
        None,
        description="创建的节点信息",
        example=None
    )


NODE_MANAGER = APIRouter()

@NODE_MANAGER.post(
    "/api/v1/node/create",
    tags=["节点管理"],
    response_model=APIOutputResponse,
    summary="当前用户登录之后生成默认节点",
    responses={
        200: {"description": "节点创建成功"},
        400: {"description": "请求参数错误"},
        422: {"description": "数据格式错误"},
    }
)
async def create_default_node(node_info: CreateNodeRequest):
    """
    创建新节点, 用户登录之后默认会创建一个基础节点
    """
    # 业务逻辑处理
    return APIOutputResponse()
