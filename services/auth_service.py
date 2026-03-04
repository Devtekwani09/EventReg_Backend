from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.users import Users
from utils.security import (
    hash_password, verify_password,
    generate_otp, create_access_token,
    create_refresh_token
)
from utils.send_email import send_verification_email
from jose import jwt, JWTError
from config import settings

def register_user(data, db: Session):
    existing = db.query(Users).filter(Users.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    otp = generate_otp()

    user = Users(
        email=data.email,
        password=hash_password(data.password),
        company_name=data.company_name,
        verification_code=otp
    )

    db.add(user)
    db.commit()

    send_verification_email(data.email, otp)

    return {"message": "User registered. Please verify OTP sent to email."}

def regenerate_verification_otp(email: str, db: Session):
    user = db.query(Users).filter(Users.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = generate_otp()
    user.verification_code = otp
    db.commit()

    send_verification_email(email, otp)

    return {"message": "New OTP sent to email"}


def verify_user(email: str, otp: str, db: Session):
    user = db.query(Users).filter(Users.email == email).first()
    if not user or user.verification_code != otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    user.is_verified = True
    user.verification_code = None
    db.commit()

    return {"message": "Email verified successfully"}


def login_user(data, db: Session):
    user = db.query(Users).filter(Users.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not user.is_verified:
        raise HTTPException(status_code=400, detail="Email not verified")

    access_token = create_access_token({"sub": user.email})
    refresh_token = create_refresh_token({"sub": user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


def regenerate_access_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        new_access_token = create_access_token({"sub": email})
        return {"access_token": new_access_token}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
    
def get_all_users(db: Session):
    users = db.query(Users).all()
    return users

def change_user_password(user, current_password: str, new_password: str, db):
    # Verify old password
    if not verify_password(current_password, user.password):
        return "invalid_password"

    # Optional: prevent same password reuse
    if verify_password(new_password, user.password):
        return "same_password"

    # Hash new password
    user.password = hash_password(new_password)

    db.commit()
    db.refresh(user)

    return "success"

def change_user_password(user, current_password: str, new_password: str, db):
    # Verify old password
    if not verify_password(current_password, user.password):
        return "invalid_password"

    # Optional: prevent same password reuse
    if verify_password(new_password, user.password):
        return "same_password"

    # Hash new password
    user.password = hash_password(new_password)

    db.commit()
    db.refresh(user)

    return "success"