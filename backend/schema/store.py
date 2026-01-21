import uuid

from pydantic import BaseModel

from backend.domain.store import StoreStatus
from backend.schema.base import BaseRequest


class StoreCreateRequest(BaseRequest):
    name: str
    business_id: uuid.UUID


class StoreDeleteRequest(BaseRequest):
    id: uuid.UUID


class StoreUpdateRequest(BaseRequest):
    id: uuid.UUID
    name: str


class StoreGetByNameInBusinessRequest(BaseRequest):
    name: str
    business_id: uuid.UUID


class StoreAllByBusinessRequest(BaseRequest):
    business_id: uuid.UUID


class StoreResponse(BaseModel):
    id: uuid.UUID
    business_id: uuid.UUID
    name: str
    status: StoreStatus


class StoreListResponse(BaseModel):
    storees: list[StoreResponse]
