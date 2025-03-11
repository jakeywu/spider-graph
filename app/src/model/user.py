from sqlalchemy import Column, String, Boolean, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from src.db.pgsql.session import Base
from datetime import datetime, UTC

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    mobile = Column(String(20), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(String(128))
    nickname = Column(String(50), nullable=False)
    full_name = Column(String(100))
    description = Column(Text)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC))


class LoginHistory(Base):
    __tablename__ = "login_histories"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), index=True)
    login_at = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(20))
    login_method = Column(String(20))
    device_info = Column(Text)
    status = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



