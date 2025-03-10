from fastapi import APIRouter, HTTPException
from datetime import datetime, UTC
from src.utils.output import api_output, OutputResponse
from pydantic import BaseModel, Field
from typing import Dict, Any


# 创建节点请求模型
class CreateNodeModel(BaseModel):
    label: str = Field("Person", description="节点的标签，例如 'Person'")
    properties: Dict[str, Any] = Field(
        default={
            "name": "朱元璋",
            "birth_year": 1328,
            "birth_place": "濠州钟离",
            "title": "明太祖"
        },
        description="节点的属性键值对"
    )


NODE_MANAGER = APIRouter()


@NODE_MANAGER.post(
    "/api/v1/node/create",
    response_model=OutputResponse,
    responses={
        200: {"description": "节点创建成功"},
        400: {"description": "请求参数错误，可能是 properties 为空或格式不正确"},
        422: {"description": "请求数据格式错误，例如数据类型不匹配"},
        500: {"description": "服务器内部错误"}
    },
)
async def create_node(node_info: CreateNodeModel):
    """
    用户登录之后，创建默认节点。

    - **label**: 节点的类型，默认值为 `"Person"`
    - **properties**: 节点的属性，必须是一个字典
    
    **可能的错误:**
    - `400`: 如果 `properties` 为空或格式错误
    - `422`: 如果 `label` 或 `properties` 的数据类型错误
    - `500`: 服务器内部错误
    """
    
    # 检查 properties 是否为空
    if not node_info.properties:
        raise HTTPException(status_code=400, detail="properties 不能为空")

    result = {
        "id": "node001",
        "label": node_info.label,
        "properties": node_info.properties,
        "created_at": datetime.now(UTC).isoformat()
    }
    
    return api_output(data=result)

