from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.settings.load_env import env

# 对特殊字符进行URL编码
safe_user = quote_plus(env.postgres.POSTGRES_USER)       # "spiderGraph!" -> "spiderGraph%21"
safe_pass = quote_plus(env.postgres.POSTGRES_PASSWORD)   # "!@#sGEWQ123" -> "%21%40%23sGEWQ123"

# 构建数据库连接URL
DATABASE_URL = f"postgresql://{safe_user}:{safe_pass}@{env.postgres.POSTGRES_HOST}:{env.postgres.POSTGRES_PORT}/{env.postgres.POSTGRES_DB}"

# 创建数据库引擎（带连接池配置）
engine = create_engine(
    DATABASE_URL,
    pool_size=10,            # 连接池保持10个连接
    max_overflow=5,          # 允许临时增加5个连接
    pool_pre_ping=True,      # 执行前检查连接有效性
    connect_args={           # 设置连接超时参数
        "connect_timeout": 10
    }
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
