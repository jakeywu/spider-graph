from fastapi import APIRouter, Body
from typing import Optional
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from src.schemas.graph import CreateRelationRequest, CreateRelationAndNodeResponse
import uuid

GRAPH_MANAGER = APIRouter()

# 安全配置（需要根据实际环境配置）


class APIOutputResponse(BaseModel):
    code: int = Field(200, description="API状态码")
    message: str = Field("success", description="API响应消息")
    data: Optional[CreateRelationAndNodeResponse] = Field(
        None,
        description="查看图信息",
        example=None
    )

GRAPH_MANAGER = APIRouter()

@GRAPH_MANAGER.post(
    "/api/v1/ran/create",
    tags=["图管理"],
    response_model=APIOutputResponse,
    summary="基于某个节点创建与其相关的节点及其关系",
    responses={
        200: {"description": "查看图成功"},
        400: {"description": "请求参数错误"},
        422: {"description": "数据格式错误"},
    }
)
async def create_node_and_relation(relation_and_node: CreateRelationRequest):
    """
    查看图节点及其关系
    """
    return CreateRelationAndNodeResponse()