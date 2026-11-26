from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal

# Restrict roles to only these three valid values
RoleType = Literal["employee", "manager", "admin"]

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: RoleType = "employee"

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str