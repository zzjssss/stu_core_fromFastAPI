from typing import TypeVar, Generic
from pydantic import BaseModel

# 1. 定义泛型类型变量，代表业务数据的具体类型
T = TypeVar("T")

# 2. 定义基础响应模型，继承 Generic[T]
class ApiResponse(BaseModel, Generic[T]):
    code: int = 200
    msg: str = "success"
    data: T = None

# 3. 实际业务中使用
class UserOut(BaseModel):
    id: int
    name: str

# 此时 UserResponse 的 data 字段会被精准推断为 UserOut 类型
UserResponse = ApiResponse[UserOut]

# 测试
# valid_data = {"code": 200, "msg": "ok", "data": {"id": 1, "name": "test"}}
# resp = UserResponse(**valid_data)
# 如果 data 里面缺了 name，Pydantic 会直接报 ValidationError
