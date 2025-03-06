import uvicorn
from src.settings.c_logger import LOG_CONFIGURE
from src.routers.health import HEALTH_ROUTER
from src.routers.auth import AUTH_ROUTER
from src.routers.user import USER_ROUTER
from src.settings.load_env import env
from fastapi import FastAPI


APP = FastAPI()


if __name__ == "__main__":
    APP.include_router(HEALTH_ROUTER)
    APP.include_router(AUTH_ROUTER)
    APP.include_router(USER_ROUTER)
    uvicorn.run(
        app=APP,
        host=env.system.SERVER_HOST,
        port=env.system.SERVER_PORT,
        log_config=LOG_CONFIGURE
    )

