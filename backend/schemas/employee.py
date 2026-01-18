import uuid

from pydantic import BaseModel, EmailStr

from backend.domain.employee import EmployeeStatus


class EmployeeCreateRequest(BaseModel):
    email: EmailStr
    name: str
    password: str
    business_id: uuid.UUID

    class Config:
        from_attributes = True


class EmployeeDeleteRequest(BaseModel):
    email: EmailStr


class EmployeeGetByEmailRequest(BaseModel):
    email: EmailStr


class EmployeeGetByIDRequest(BaseModel):
    id: uuid.UUID


class EmployeeResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    name: str
    status: EmployeeStatus

    class Config:
        from_attributes = True


class EmployeeListResponse(BaseModel):
    employeees: list[EmployeeResponse]
