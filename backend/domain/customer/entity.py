import uuid

from sqlalchemy import UUID, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.domain.base.entity import BaseModel

from .enum import CustomerStatus


class Customer(BaseModel):
    __tablename__ = "customers"

    name: Mapped[str] = mapped_column(String(63))

    phone: Mapped[str] = mapped_column(unique=True, index=True)

    status: Mapped[CustomerStatus] = mapped_column(
        Enum(CustomerStatus, name="business_status"),
        nullable=False,
        default=CustomerStatus.ACTIVATED,
    )


class CustomerGift(BaseModel):
    __tablename__ = "customer_gift"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("customers.id"),
        primary_key=True,
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        primary_key=True,
    )

    count: Mapped[int] = mapped_column(default=0)


class CustomerPoints(BaseModel):
    __tablename__ = "customer_points"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("customers.id"),
        primary_key=True,
    )

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id"),
        primary_key=True,
    )

    points: Mapped[int] = mapped_column(default=0)
