from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class Token(BaseModel):
    access_token: str
    token_type: str

# Pydantic模型
class UserBase(BaseModel):
    mobile: Optional[str]
    email: Optional[EmailStr]
    nickname: str

class UserCreateMobile(BaseModel):
    mobile: str
    verification_code: str

class UserCreateEmail(BaseModel):
    email: EmailStr

class UserActivate(BaseModel):
    email: EmailStr
    activation_code: str
    password: str

class PasswordUpdate(BaseModel):
    password: str
    new_password: str

class PasswordReset(BaseModel):
    email: EmailStr
    password: str
    new_password: str

class TokenData(BaseModel):
    user_id: Optional[UUID] = None
