from fastapi import APIRouter, Query
from src.utils.output import APIOutputResponse
from src.schemas.graph import ViewGraphResponse, CreateRelationRequest, CreateRelationAndNodeResponse

GRAPH_MANAGER = APIRouter()


@GRAPH_MANAGER.get(
    "/api/v1/view/clique",
    tags=["团管理"],
    response_model=APIOutputResponse[ViewGraphResponse],
    summary="查看某个节点的图信息",
    responses={
        200: {"description": "查看图成功"},
        400: {"description": "请求参数错误"},
        422: {"description": "数据格式错误"},
    }
)
async def view_graph_by_node_id(node_id: str = Query(default="NODE_001", description="节点 ID"), node_type: str = Query(default="Person", description="节点类型")):
    """
    查看图节点及其关系
    """
    result = {
        "code": 200,
        "message": "success",
        "data": {
            "nodes": [
            {
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
                ],
                "links": [
                {
                    "source": "NODE_001",
                    "target": "NODE_003",
                    "relation_type": "父亲"
                }
                ]
            }
        }
    return APIOutputResponse(**result)


@GRAPH_MANAGER.post(
    "/api/v1/ran/create",
    tags=["团管理"],
    response_model=APIOutputResponse[CreateRelationAndNodeResponse],
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
    result = {
        "code": 200,
        "message": "success",
        "data": {
            "nodes": [
                {
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
                ],
                "links": [
                {
                    "source": "NODE_001",
                    "target": "NODE_003",
                    "relation_type": "父亲"
                }
                ]
            }
        }
    return APIOutputResponse(**result)