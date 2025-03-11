from pydantic import BaseModel, Field
from typing import Dict, Any, List
from datetime import datetime


class CreateNodeRequest(BaseModel):
    """
    创建默认节点请求
    """
    node_type: str = Field(
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


class NodeResponse(BaseModel):
    """
    创建默认节点响应
    """
    node_id: str = Field(
        description="节点唯一标识符（UUID v4）",
        example="550e8400-e29b-41d4-a716-446655440000"
    )
    created_at: datetime = Field(
        description="节点创建时间",
        example="2023-10-05T08:00:00+00:00"
    )
    node: CreateNodeRequest = Field(
        ...,
        description="节点信息"
    )


class NodeRelation(BaseModel):
    """
    关联的单个节点及其关系
    """
    relation: str = Field(
        ...,
        description="节点之间的关系",
        example="父亲",
    )
    node: CreateNodeRequest = Field(
        ...,
        description="关联的节点信息"
    )


class CreateRelationRequest(BaseModel):
    """
    创建关系的请求
    """
    node_id: str = Field(
        ...,
        description="源节点ID",
        example="NODE_001"
    )
    relations: List[NodeRelation] = Field(
        ...,
        description="该节点与其他节点的所有关系"
    )


class RelationResponse(BaseModel):
    """
    关系返回结构
    """
    source: str = Field(
        description="源节点ID",
        example="NODE_001"
    )
    target: str = Field(
        description="目标节点ID",
        example="NODE_003"
    )
    relation_type: str = Field(
        description="关系类型",
        example="父亲"
    )


class CreateRelationAndNodeResponse(BaseModel):
    """
    关联图数据返回
    """
    nodes: List[NodeResponse] = Field(
        ...,
        description="创建的节点列表",
    )
    links: List[RelationResponse] = Field(
        ...,
        description="创建的关系列表",
    )


class ViewGraphResponse(BaseModel):
    """
    查看图响应
    """
    nodes: List[NodeResponse] = Field(
        ...,
        description="创建的节点列表",
    )
    links: List[RelationResponse] = Field(
        ...,
        description="创建的关系列表",
    )
