from fastapi import APIRouter
from datetime import datetime, UTC
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
import uuid

# 安全配置（需要根据实际环境配置）
class CreateNodeResponse(BaseModel):
    unique_id: str = Field(
        description="节点唯一标识符（UUID v4）",
        example="550e8400-e29b-41d4-a716-446655440000"
    )
    label: str = Field(
        default="Person",
        description="节点类型标签",
        example="Person"
    )
    properties: Dict[str, Any] = Field(
        description="节点属性字典",
        example={
            "name": "朱元璋",
            "birth_year": 1328,
            "birth_place": "濠州钟离",
            "title": "明太祖"
        }
    )
    created_at: datetime = Field(
        description="节点创建时间",
        example="2023-10-05T08:00:00+00:00"
    )

class CreateNodeModel(BaseModel):
    label: str = Field(
        "Person",
        description="节点类型标签",
        example="Person"
    )
    properties: Dict[str, Any] = Field(
        description="节点属性字典",
        example={
            "name": "朱元璋",
            "birth_year": 1328,
            "birth_place": "濠州钟离",
            "title": "明太祖"
        }
    )

class OutputResponse(BaseModel):
    code: int = Field(200, description="API状态码")
    message: str = Field("success", description="API响应消息")
    data: Optional[CreateNodeResponse] = Field(
        None,
        description="创建的节点信息",
        example=None
    )

    @classmethod
    def example(cls):
        return cls(
            code=200,
            message="success",
            data=CreateNodeResponse(
                unique_id=str(uuid.uuid4()),
                label="Person",
                properties={
                    "name": "朱元璋",
                    "birth_year": 1328,
                    "birth_place": "濠州钟离",
                    "title": "明太祖"
                },
                created_at=datetime.now(tz=UTC).isoformat()
            )
        )
    

NODE_MANAGER = APIRouter()

@NODE_MANAGER.post(
    "/api/v1/node/create",
    tags=["节点管理"],
    response_model=OutputResponse,
    summary="当前用户登录之后生成默认节点",
    responses={
        200: {"description": "节点创建成功", "example": OutputResponse.example()},
        400: {"description": "请求参数错误", "example": {"code": 400, "message": "Invalid request parameters"}},
        422: {"description": "数据格式错误", "example": {"code": 422, "message": "Validation error"}},
    }
)
async def create_default_node(node_info: CreateNodeModel):
    """
    创建新节点, 用户登录之后默认会创建一个基础节点

    ​**错误场景**:
    - 401: 未提供有效认证令牌
    - 400/422: 参数验证失败
    - 500: 服务器内部错误
    """
    # 业务逻辑处理
    created_node = CreateNodeResponse(
        unique_id=str(uuid.uuid4()),
        label=node_info.label,
        properties=node_info.properties,
        created_at=datetime.now(UTC).isoformat()
    )
    return OutputResponse(code=200, message="success", data=created_node).model_dump()
