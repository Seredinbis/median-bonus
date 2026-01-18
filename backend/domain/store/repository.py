from typing import TYPE_CHECKING

from sqlalchemy import and_, select

from backend.domain.base.repository import BaseRepository
from backend.domain.store import Store, StoreStatus

if TYPE_CHECKING:
    import uuid


class StoreRepository(BaseRepository):
    async def get_by_name(self, name: str, business_id: "uuid.UUID") -> Store | None:
        result = await self.session.execute(
            select(Store).where(
                and_(
                    Store.business_id == business_id,
                    Store.name == name,
                    Store.status != StoreStatus.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_by_id(self, id: "uuid.UUID") -> Store | None:
        result = await self.session.execute(select(Store).where(Store.id == id))
        return result.scalar_one_or_none()

    async def get_all(self, business_id: "uuid.UUID") -> list[Store | None]:
        result = await self.session.execute(
            select(Store).where(
                and_(
                    Store.business_id == business_id,
                    Store.status != StoreStatus.SUSPENDED,
                )
            )
        )
        return list(result.scalars().all())
