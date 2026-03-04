from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import RegisterSchema, LoginSchema, VerifySchema, UserResponse, ChangePasswordRequest
from services.auth_service import (
    register_user, login_user,
    regenerate_access_token, verify_user, regenerate_verification_otp, get_all_users, change_user_password
)
from typing import List
from utils.dependencies import get_current_user


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    return register_user(data, db)

@router.post("/verify")
def verify(data: VerifySchema, db: Session = Depends(get_db)):
    return verify_user(data.email, data.otp, db)

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    return login_user(data, db)

@router.post("/refresh")
def refresh(refresh_token: str):
    return regenerate_access_token(refresh_token)

@router.post("/generate-otp")
def generate_otp_api(email: str, db: Session = Depends(get_db)):
    return regenerate_verification_otp(email, db)

@router.get("/get_all_users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.post("/change-password")
def change_password(
    data: ChangePasswordRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return change_user_password(current_user, data.current_password, data.new_password, db)