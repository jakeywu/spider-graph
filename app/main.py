import uvicorn
from fastapi import FastAPI
from src.routers.health import HEALTH_ROUTER
from src.routers.auth import AUTH_ROUTER
from src.routers.user import USER_ROUTER
from src.routers.node_manager import NODE_MANAGER
from src.routers.graph_manager import GRAPH_MANAGER
from src.settings.load_env import env

# 创建 FastAPI 实例
APP = FastAPI(
    title="族谱关系维护API",
    description="""所有后端API都会基于该文档进行管理，在正式具体接口功能之前，都会预先定义好输入输出接口。\n相关文档:
    [原型说明文档](https://v0.dev/chat/family-tree-55Jlpju3SKn?b=b_UbNoCuL2O0X)""",
)

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
