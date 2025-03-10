import uvicorn
from fastapi import FastAPI
from src.routers.health import HEALTH_ROUTER
from src.routers.auth import AUTH_ROUTER
from src.routers.user import USER_ROUTER
from src.routers.node_manager import NODE_MANAGER
from src.routers.graph_manager import GRAPH_MANAGER
from src.settings.load_env import env

# 创建 FastAPI 实例
APP = FastAPI()

# 注册路由
# APP.include_router(HEALTH_ROUTER)
# APP.include_router(AUTH_ROUTER)
APP.include_router(NODE_MANAGER)
APP.include_router(GRAPH_MANAGER)


# 仅在直接运行 main.py 时使用 uvicorn 启动
if __name__ == "__main__":
    uvicorn.run(
        "main:APP",  # 这里使用 "main:APP" 以兼容 `fastapi run main.py` 和 `fastapi dev main.py`
        host=env.system.SERVER_HOST,
        port=env.system.SERVER_PORT,
        reload=True  # 便于开发时热重载
    )
