import uuid
from typing import TYPE_CHECKING

from sqlalchemy import and_, select

from backend.domain.base.repository import BaseRepository
from backend.domain.employee import Employee, EmployeeStatus

if TYPE_CHECKING:
    import uuid


class EmployeeRepository(BaseRepository):
    async def get_by_email(self, email: str) -> Employee | None:
        result = await self.session.execute(
            select(Employee).where(
                and_(
                    Employee.email == email,
                    Employee.status != EmployeeStatus.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_by_id(self, id: "uuid.UUID") -> Employee | None:
        result = await self.session.execute(
            select(Employee).where(
                and_(
                    Employee.id == id,
                    Employee.status != EmployeeStatus.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Employee | None]:
        result = await self.session.execute(select(Employee).where(Employee.status != EmployeeStatus.SUSPENDED))
        return list(result.scalars().all())
