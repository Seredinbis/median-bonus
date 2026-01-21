import uuid

from pydantic import BaseModel

from backend.schema.base import BaseRequest


class CustomerCreateRequest(BaseRequest):
    phone: str
    name: str | None


class CustomerUpdateRequest(BaseRequest):
    id: uuid.UUID
    phone: str | None
    name: str | None


class CustomerDeleteRequest(BaseRequest):
    id: uuid.UUID


class CustomerGetByPhoneRequest(BaseRequest):
    phone: str


class CustomerResponse(BaseModel):
    id: uuid.UUID
    phone: str
    name: str | None


class CustomerListResponse(BaseModel):
    customers: list[CustomerResponse]
