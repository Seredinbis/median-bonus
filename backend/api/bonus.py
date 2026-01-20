from fastapi import APIRouter, Depends, status

from backend.factories.service import get_bonus_service
from backend.schemas.bonus import (
    BonusCreateRequest,
    BonusDeleteRequest,
    BonusGetByIDRequest,
    BonusListResponse,
    BonusResponse,
)
from backend.services.bonus import BonusService

router = APIRouter(prefix="/bonus", tags=["bonus"])


# All APIs consist of POST methods due to the future need for RBAC and JWT verification.
# TODO: RBAC, JWT


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=BonusResponse,
)
async def create(
    data: BonusCreateRequest,
    service: BonusService = Depends(get_bonus_service),
) -> BonusResponse:
    return await service.create(data)


@router.post(
    "/delete",
    status_code=status.HTTP_200_OK,
    response_model=BonusResponse,
)
async def delete(
    data: BonusDeleteRequest,
    service: BonusService = Depends(get_bonus_service),
) -> BonusResponse | None:
    return await service.delete(data)


@router.post(
    "/get_by_id",
    status_code=status.HTTP_200_OK,
    response_model=BonusResponse,
)
async def get_by_id(
    data: BonusGetByIDRequest,
    service: BonusService = Depends(get_bonus_service),
) -> BonusResponse | None:
    return await service.get(data)


@router.post(
    "/get_all",
    status_code=status.HTTP_200_OK,
    response_model=BonusListResponse,
)
async def get_all(
    service: BonusService = Depends(get_bonus_service),
) -> BonusListResponse:
    return await service.get_all()
