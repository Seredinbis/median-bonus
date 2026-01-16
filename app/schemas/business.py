from pydantic import BaseModel, EmailStr

from app.domain.business import Status


class BusinessCreate(BaseModel):
    email: EmailStr
    password_hash: str


class BusinessRead(BaseModel):
    id: int
    email: EmailStr
    is_active: Status

    class Config:
        from_attributes = True
