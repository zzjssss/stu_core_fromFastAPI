from fastapi import FastAPI, Depends
from loguru import logger

# 全局基础设施：必须先 setup_logging，之后的所有日志（含 uvicorn 以外的业务日志）都走 loguru
from src.my_model.core import (
    settings,
    Logger,
    setup_logging,
    ok,
    BusinessError,
    register_exception_handlers,
)

setup_logging()

app = FastAPI(title=settings.APP_NAME)

# 注册全局异常处理器：业务异常/HTTP异常/校验异常/未捕获异常 -> 统一 {code,msg,data} 响应
register_exception_handlers(app)


@app.get("/")
async def root(logger=Depends(Logger)):
    logger.info("root 被调用")
    return ok(data={"message": "Hello World"})


@app.get("/hello/{name}")
async def say_hello(name: str, logger=Depends(Logger)):
    logger.debug(f"say_hello 参数: name={name}")
    if name == "error":
        # 演示业务异常：会被全局处理器捕获成统一响应
        raise BusinessError(msg="不允许的名称", code=40001)
    return ok(data={"message": f"Hello {name}"})


if __name__ == '__main__':
    import uvicorn
    logger.info(f"启动 {settings.APP_NAME} ({settings.APP_ENV})")
    uvicorn.run(app, host="0.0.0.0", port=8001)
