from sqlalchemy import select

from backend.domain.base.repository import BaseRepository
from backend.domain.customer.entity import Customer


class CustomerRepository(BaseRepository):
    async def get_by_phone(self, phone: str) -> Customer | None:
        result = await self.session.execute(select(Customer).where(Customer.phone == phone))
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Customer | None]:
        result = await self.session.execute(select(Customer))
        return list(result.scalars().all())
