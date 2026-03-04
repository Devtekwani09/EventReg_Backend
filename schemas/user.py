from pydantic import BaseModel, EmailStr
from datetime import datetime

class RegisterSchema(BaseModel):
    email: EmailStr
    password: str
    company_name: str

class VerifySchema(BaseModel):
    email: EmailStr
    otp: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: int
    email: str
    is_verified: bool

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str