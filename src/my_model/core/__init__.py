"""core 包：全局基础设施（配置、日志），与业务无关，可直接复制到新项目。"""
from src.my_model.core.settings import settings
from src.my_model.core.logger import Logger, setup_logging

__all__ = ["settings", "Logger", "setup_logging"]
