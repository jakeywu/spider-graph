from typing import Any
from pydantic import BaseModel, Field
from fastapi import HTTPException
from typing import Optional


# --- 通用响应模型 ---
class OutputResponse(BaseModel):
    code: int = Field(200, description="API 状态码")
    message: str = Field("success", description="API 状态信息")
    data: Optional[Any] = Field(None, description="响应数据")


def api_output(
    data: Optional[Any] = None,
    message: str = "success",
    code: int = 200
) -> OutputResponse:
    """统一 API 响应格式"""
    return OutputResponse(
        code=code,
        message=message.lower(),
        data=data
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
