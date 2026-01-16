from fastapi import APIRouter, Depends, status

from app.factories.business import get_business_service
from app.schemas.business import BusinessCreate
from app.services.business import BusinessService


router = APIRouter(tags=["business"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
async def register_business(
    data: BusinessCreate,
    service: BusinessService = Depends(get_business_service),
):
    return await service.register(data)
