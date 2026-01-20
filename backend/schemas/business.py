import uuid

from pydantic import BaseModel, EmailStr

from backend.domain.business import BusinessStatus
from backend.schemas.base import BaseRequest


class BusinessCreateRequest(BaseRequest):
    email: EmailStr
    name: str
    password: str


class BusinessUpdateRequest(BaseRequest):
    id: uuid.UUID
    email: EmailStr | None
    name: str | None
    password: str | None


class BusinessDeleteRequest(BaseRequest):
    id: uuid.UUID


class BusinessGetByEmailRequest(BaseRequest):
    email: EmailStr


class BusinessResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    name: str
    status: BusinessStatus


class BusinessListResponse(BaseModel):
    businesses: list[BusinessResponse]
