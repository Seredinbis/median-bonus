from fastapi import Depends

from app.domain.business import BusinessRepository
from app.services.business import BusinessService
from .repository import get_business_repository


def get_business_service(
    repository: BusinessRepository = Depends(get_business_repository),
) -> BusinessService:
    return BusinessService(repository)
