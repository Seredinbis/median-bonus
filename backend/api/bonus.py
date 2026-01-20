import uuid

from fastapi import APIRouter, Depends, status

from backend.factories.service import get_bonus_service
from backend.schemas.bonus import (
    BonusCreateRequest,
    BonusDeleteRequest,
    BonusListResponse,
    BonusResponse,
    BonusUpdateRequest,
)
from backend.services.bonus import BonusService

router = APIRouter(prefix="/bonus", tags=["bonus"])


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


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=BonusResponse,
)
async def update(
    data: BonusUpdateRequest,
    service: BonusService = Depends(get_bonus_service),
) -> BonusResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=BonusResponse,
)
async def delete(
    data: BonusDeleteRequest,
    service: BonusService = Depends(get_bonus_service),
) -> BonusResponse | None:
    return await service.delete(data)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=BonusResponse,
)
async def get(
    id: uuid.UUID,  # noqa
    service: BonusService = Depends(get_bonus_service),
) -> BonusResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=BonusListResponse,
)
async def get_all(
    service: BonusService = Depends(get_bonus_service),
) -> BonusListResponse:
    return await service.get_all()
