from fastapi import APIRouter, Path
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from src.utils.output import OutputResponse, api_output


# --- 节点/关系模型 ---
class NodeModel(BaseModel):
    id: str = Field(..., description="节点唯一ID")
    label: str = Field("Person", description="节点类型")
    properties: Dict[str, Any] = Field(..., description="节点属性")

class LinkModel(BaseModel):
    source: str = Field(..., description="源节点ID")
    target: str = Field(..., description="目标节点ID")
    type: str = Field(..., description="关系类型")

class GraphData(BaseModel):
    nodes: List[NodeModel] = Field(..., description="节点列表")
    links: List[LinkModel] = Field(..., description="关系列表")

# --- 模拟数据库数据 ---
MOCK_DATA = GraphData(
    nodes=[
        NodeModel(
            id="NODE_003",
            label="Person",
            properties={
                "name": "朱棣",
                "birth_year": 1360,
                "birth_place": "应天府",
                "title": "明成祖"
            }
        ),
        # 其他关联节点...
    ],
    links=[
        LinkModel(
            source="NODE_003",
            target="NODE_001",
            type="Father"
        ),
        # 其他关系...
    ]
)


class OutputResponse(BaseModel):
    code: int = Field(200, description="API状态码")
    message: str = Field("success", description="API响应消息")
    data: Optional[GraphData] = Field(
        None,
        description="查看某个节点的图",
        example=None
    )

    @classmethod
    def example(cls):
        return cls(
            code=200,
            message="success",
            data=MOCK_DATA
        )
    
# --- API 路由 ---
GRAPH_MANAGER = APIRouter()



# --- 图谱查询接口 ---
@GRAPH_MANAGER.get(
    "/api/v1/{node_id}/graph",
    tags=["团管理"],
    response_model=OutputResponse,
    summary="查询当前节点所在完整团",
    responses={
        200: {"description": "成功返回图谱数据", "example": OutputResponse.example()},
        400: {"description": "请求参数错误", "example": {"code": 400, "message": "Invalid request parameters"}},
        422: {"description": "数据格式错误", "example": {"code": 422, "message": "Validation error"}},
    }
)
async def get_graph_by_node_id(
    node_id: str = Path(..., min_length=3, example="NODE_003", description="节点唯一标识符")
) -> OutputResponse:
    """
    获取指定节点的关联图谱
    
    - **node_id**: 节点唯一标识符（示例：NODE_003）
    """
    return OutputResponse(code=200, message="success", data=MOCK_DATA).model_dump()
