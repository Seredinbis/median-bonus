from typing import TYPE_CHECKING

from sqlalchemy import and_, select

from backend.domain.base.repository import BaseRepository
from backend.domain.business import Business, BusinessStatus

if TYPE_CHECKING:
    import uuid


class BusinessRepository(BaseRepository):
    async def get_by_email(self, email: str) -> Business | None:
        result = await self.session.execute(
            select(Business).where(
                and_(
                    Business.email == email,
                    Business.status != BusinessStatus.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_by_id(self, id: "uuid.UUID") -> Business | None:
        result = await self.session.execute(
            select(Business).where(
                and_(
                    Business.id == id,
                    Business.status != BusinessStatus.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Business | None]:
        result = await self.session.execute(select(Business).where(Business.status != BusinessStatus.SUSPENDED))
        return list(result.scalars().all())
