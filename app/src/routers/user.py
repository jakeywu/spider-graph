from fastapi import APIRouter, Depends, HTTPException
from src.schemas.auth import PasswordUpdate
from src.core.security import get_current_user
from src.db.pgsql.session import get_db
from src.model.user import User
from src.utils.password import get_password_hash, verify_password

USER_ROUTER = APIRouter(prefix="/user", tags=["User"])


@USER_ROUTER.put("/me/password")
async def update_password(
    password_update: PasswordUpdate,
    current_user: User = Depends(get_current_user),
    db = Depends(get_db)
):
    if not verify_password(password_update.old_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect old password")
    
    current_user.password_hash = get_password_hash(password_update.new_password)
    db.commit()
    return {"message": "Password updated successfully"}