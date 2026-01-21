import uuid

from pydantic import BaseModel

from backend.domain.product import ProductStatus
from backend.domain.product.enum import Category
from backend.schema.base import BaseRequest


class ProductCreateRequest(BaseRequest):
    name: str
    store_id: uuid.UUID
    category: Category
    price: float


class ProductUpdateRequest(BaseRequest):
    id: uuid.UUID
    name: str | None
    category: Category | None
    price: float | None


class ProductDeleteRequest(BaseRequest):
    id: uuid.UUID


class ProductGetByNameInStoreRequest(BaseRequest):
    name: str
    store_id: uuid.UUID


class ProductAllByStoreRequest(BaseRequest):
    store_id: uuid.UUID


class ProductResponse(BaseModel):
    id: uuid.UUID
    store_id: uuid.UUID
    name: str
    status: ProductStatus
    category: Category
    price: float


class ProductListResponse(BaseModel):
    productes: list[ProductResponse]
