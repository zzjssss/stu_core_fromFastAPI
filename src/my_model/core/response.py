"""统一响应格式：全站接口返回 {code, msg, data} 结构。

使用方式一（直接返回字典）：
    from src.my_model.core.response import ok, fail
    return ok(data={"id": 1})            # {"code":0,"msg":"success","data":{...}}
    return fail(msg="用户名已存在", code=40901)

使用方式二（作为 response_model，配合泛型）：
    from src.my_model.core.response import ResponseModel
    @app.get("/user", response_model=ResponseModel[UserOut])
    ...
"""
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    """通用响应体模型（用于 OpenAPI 文档 / response_model）"""
    code: int = 0
    msg: str = "success"
    data: Optional[T] = None


def ok(data=None, msg: str = "success", code: int = 0) -> dict:
    """成功响应"""
    return {"code": code, "msg": msg, "data": data}


def fail(msg: str = "error", code: int = 1, data=None) -> dict:
    """失败响应（HTTP 状态由异常处理器或调用方决定，这里只负责结构）"""
    return {"code": code, "msg": msg, "data": data}
