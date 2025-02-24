import uvicorn
from app.src.settings.c_logger import LOG_CONFIGURE
from app.src.routers.health import pcc_router
from app.src.initial.load_env import env
from fastapi import FastAPI


APP = FastAPI()


if __name__ == "__main__":
    APP.include_router(pcc_router)
    uvicorn.run(
        app=APP,
        host=env.system.SERVER_HOST,
        port=env.system.SERVER_PORT,
        log_config=LOG_CONFIGURE
    )

