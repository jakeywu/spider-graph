
from datetime import datetime, timedelta, UTC
from typing import Optional
from jose import jwt
from uuid import UUID
from fastapi import Depends, HTTPException, status
from src.settings.load_env import env
from src.db.pgsql.session import get_db
from src.model.user import User
from fastapi.security import OAuth2PasswordBearer
from src.schemas.auth import TokenData

SECRET_KEY = env.security.SECRET_KEY
ALGORITHM = env.security.ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: UUID = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).get(token_data.user_id)
    if user is None:
        raise credentials_exception
    return user
