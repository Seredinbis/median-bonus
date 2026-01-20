from typing import TYPE_CHECKING

from backend.domain.employee import Employee, EmployeeStatus
from backend.factories.repository import get_employee_repository
from backend.security import hash_password
from backend.utils.exception_handler import AlreadyExistsError, NotFoundError

if TYPE_CHECKING:
    import uuid

    from backend.domain.employee import EmployeeRepository
    from backend.schemas.employee import (
        EmployeeCreateRequest,
        EmployeeDeleteRequest,
        EmployeeGetByEmailRequest,
        EmployeeListResponse,
        EmployeeResponse,
        EmployeeUpdateRequest,
    )


class EmployeeService:
    def __init__(self, repository: "EmployeeRepository" = get_employee_repository()):
        self.repository = repository

    async def create(self, data: "EmployeeCreateRequest") -> EmployeeResponse:
        existing = await self.repository.get_by_email(str(data.email))
        if existing:
            raise AlreadyExistsError("Email")

        employee = Employee(
            name=data.name,
            email=str(data.email),
            password_hash=hash_password(data.password),
            business_id=data.business_id,
        )
        result = await self.repository.create(employee)

        return EmployeeResponse.model_validate(result)

    async def update(self, data: "EmployeeUpdateRequest") -> EmployeeResponse:
        existing = await self.repository.get(Employee, data.id)
        if not existing:
            raise NotFoundError("Employee")

        if data.name:
            existing.name = data.name
        if data.email:
            existing.email = str(data.email)
        if data.password:
            existing.password_hash = hash_password(data.password)

        result = await self.repository.update(existing)

        return EmployeeResponse.model_validate(result)

    async def delete(self, data: "EmployeeDeleteRequest") -> EmployeeResponse:
        existing = await self.repository.get(Employee, data.id)
        if not existing:
            raise NotFoundError("Employee")

        existing.status = EmployeeStatus.SUSPENDED
        result = await self.repository.update(existing)

        return EmployeeResponse.model_validate(result)

    async def get(self, id: "uuid.UUID") -> EmployeeResponse:  # noqa
        result = await self.repository.get(Employee, id)
        if not result:
            raise NotFoundError("Employee")

        return EmployeeResponse.model_validate(result)

    async def get_all(self) -> EmployeeListResponse:
        result = await self.repository.get_all(Employee)
        if not result:
            raise NotFoundError("Employeees")

        return EmployeeListResponse(employeees=[EmployeeResponse.model_validate(employee) for employee in result])

    async def get_by_email(self, data: "EmployeeGetByEmailRequest") -> EmployeeResponse:
        result = await self.repository.get_by_email(str(data.email))
        if not result:
            raise NotFoundError("Employee")

        return EmployeeResponse.model_validate(result)
