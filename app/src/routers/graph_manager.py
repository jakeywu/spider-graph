from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel, Field
from typing import Dict, Any, List
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

# --- API 路由 ---
GRAPH_MANAGER = APIRouter()


# --- 模拟数据库数据 ---
MOCK_DATA = {
    "NODE_003": GraphData(
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
}

# --- 图谱查询接口 ---
@GRAPH_MANAGER.get(
    "/api/v1/{node_id}/graph",
    response_model=OutputResponse,
    responses={
        200: {"model": OutputResponse, "description": "成功返回图谱数据"},
        404: {"description": "节点不存在"}
    }
)
async def get_graph(
    node_id: str = Path(..., min_length=3, example="NODE_003", description="节点唯一标识符")
) -> OutputResponse:
    """
    获取指定节点的关联图谱
    
    - **node_id**: 节点唯一标识符（示例：NODE_003）
    """
    graph = MOCK_DATA.get(node_id)
    return api_output(data=graph.model_dump())