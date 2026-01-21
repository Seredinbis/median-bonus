import uuid

from pydantic import BaseModel

from backend.schema.base import BaseRequest


class OrderProductRequest(BaseRequest):
    product_id: uuid.UUID
    quantity: int


class OrderRequest(BaseRequest):
    store_id: uuid.UUID
    customer_phone: str | None = None
    products: list[OrderProductRequest]
    use_bonus: bool = True


class OrderResponse(BaseModel):
    id: uuid.UUID
    products: list[OrderProductRequest] | None = None
    price: float
    price_with_discount: float

    points_spend: int = 0
    points_earned: int = 0

    gift: OrderProductRequest | None = None
