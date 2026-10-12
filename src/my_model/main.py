from fastapi import FastAPI, Depends
from loguru import logger

# 全局基础设施：必须先 setup_logging，之后的所有日志（含 uvicorn 以外的业务日志）都走 loguru
from src.my_model.core import settings, Logger, setup_logging

setup_logging()

app = FastAPI(title=settings.APP_NAME)


@app.get("/")
async def root(logger=Depends(Logger)):
    logger.info("root 被调用")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str, logger=Depends(Logger)):
    logger.debug(f"say_hello 参数: name={name}")
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    import uvicorn
    logger.info(f"启动 {settings.APP_NAME} ({settings.APP_ENV})")
    uvicorn.run(app, host="0.0.0.0", port=8001)
