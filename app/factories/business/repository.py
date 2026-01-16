from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.domain.business import BusinessRepository


def get_business_repository(
    session: AsyncSession = Depends(get_db),
) -> BusinessRepository:
    return BusinessRepository(session=session)
