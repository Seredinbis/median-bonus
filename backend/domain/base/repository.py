from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.base import TimestampMixin


class BaseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, business: TimestampMixin) -> TimestampMixin:
        self.session.add(business)
        await self.session.commit()
        await self.session.refresh(business)
        return business

    async def update(self, business: TimestampMixin) -> TimestampMixin:
        await self.session.commit()
        await self.session.refresh(business)
        return business
