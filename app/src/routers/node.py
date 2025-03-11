from fastapi import APIRouter
from src.utils.output import APIOutputResponse
from src.schemas.graph import CreateNodeRequest, NodeResponse


NODE_MANAGER = APIRouter()

@NODE_MANAGER.post(
    "/api/v1/node/create",
    tags=["节点管理"],
    response_model=APIOutputResponse[NodeResponse],
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
    result = {
        "code": 200,
        "message": "success",
        "data": {
            "node_id": "550e8400-e29b-41d4-a716-446655440000",
            "created_at": "2023-10-05T08:00:00+00:00",
            "node": {
            "node_type": "Person",
            "properties": {
                "birth_place": "濠州钟离",
                "birth_year": 1328,
                "name": "朱元璋",
                "title": "明太祖"
            }
            }
        }
    }
    return APIOutputResponse(**result)
