from typing import Any
from pydantic import BaseModel, Field
from fastapi import HTTPException
from typing import Optional
from typing import Generic, TypeVar, Optional

# 定义泛型类型变量
T = TypeVar('T')

class APIOutputResponse(BaseModel, Generic[T]):
    code: int = Field(200, description="API状态码")
    message: str = Field("success", description="API响应消息")
    data: Optional[T] = Field(
        description="响应数据内容"
    )


# Custom HTTPException for consistent response structure
class CustomHTTPException(HTTPException):
    """
    custom error
    """
    def __init__(self, code: int = 400, message: str = "Parameter error"):
        self.status_code = code
        self.detail = {"code": code, "message": message.lower(), "data": None}


def convert_search_result(search_result):
    """
    convert
    :param search_result:
    :return:
    """
    final_result = []
    for item in search_result:
        similarity = round(item["distance"], 3)
        file_name = item["entity"]["name"]
        final_result.append(
            {
                "id": item["id"],
                "similarity": similarity,
                "file_name": file_name
            }
        )
    return final_result
