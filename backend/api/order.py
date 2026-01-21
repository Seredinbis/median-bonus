from fastapi import APIRouter, Depends, status

from backend.factoriy.service import get_bonus_service
from backend.schema.order import OrderRequest, OrderResponse
from backend.service.order import OrderService

router = APIRouter(prefix="/order", tags=["order"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=OrderResponse,
)
async def create(
    data: OrderRequest,
    service: OrderService = Depends(get_bonus_service),
) -> OrderResponse:
    return await service.create(data)
