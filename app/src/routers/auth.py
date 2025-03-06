from fastapi import APIRouter, Depends, HTTPException, Request
from src.schemas.auth import UserCreateMobile, UserCreateEmail, UserActivate, UserBase
from src.core.security import create_access_token
from src.db.pgsql.session import get_db
from src.model.user import User, LoginHistory
from src.utils.sms import verify_sms_code
from src.utils.email import send_activation_email, verify_activation_code
from src.utils.password import get_password_hash
from src.settings.load_env import env
from datetime import timedelta

AUTH_ROUTER = APIRouter(prefix="/auth", tags=["authentication"])

@AUTH_ROUTER.post("/register/mobile", response_model=UserBase)
async def register_mobile(user: UserCreateMobile, db = Depends(get_db)):
    # 这里需要实现短信验证码验证逻辑
    if not verify_sms_code(user.mobile, user.verification_code):
        raise HTTPException(status_code=400, detail="Invalid verification code")
    
    db_user = db.query(User).filter(User.mobile == user.mobile).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Mobile already registered")
    
    new_user = User(
        mobile=user.mobile,
        nickname=f"user_{user.mobile[-4:]}",
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@AUTH_ROUTER.post("/register/email", response_model=UserBase)
async def register_email(user: UserCreateEmail, db = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        email=user.email,
        nickname=f"user_{user.email.split('@')[0]}",
        is_active=False
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # 发送激活邮件
    send_activation_email(user.email)
    return new_user

@AUTH_ROUTER.post("/email/activate")
async def activate_account(activation: UserActivate, db = Depends(get_db)):
    user = db.query(User).filter(User.email == activation.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.is_active:
        raise HTTPException(status_code=400, detail="Account already activated")
    
    # 验证激活码
    if not verify_activation_code(activation.email, activation.activation_code):
        raise HTTPException(status_code=400, detail="Invalid activation code")
    
    user.password_hash = get_password_hash(activation.password)
    user.is_active = True
    db.commit()
    return {"message": "Account activated successfully"}

@AUTH_ROUTER.post("/login/mobile")
async def login_mobile(request: Request, mobile: str, code: str, db = Depends(get_db)):
    # 验证短信验证码
    if not verify_sms_code(mobile, code):
        raise HTTPException(status_code=400, detail="Invalid verification code")
    
    user = db.query(User).filter(User.mobile == mobile).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 记录登录历史
    login_history = LoginHistory(
        user_id=user.id,
        ip_address=request.client.host,
        login_method="mobile"
    )
    db.add(login_history)
    db.commit()
    
    access_token = create_access_token(
        data={"sub": str(user.id)}, 
        expires_delta=timedelta(minutes=env.security.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}
