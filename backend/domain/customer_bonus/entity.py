import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.domain.base import Base


class CustomerBonus(Base):
    __tablename__ = "customer_bonus"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("customers.id"),
        primary_key=True,
    )

    bonus_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("bonuses.id"),
        primary_key=True,
    )

    value: Mapped[int] = mapped_column(default=0)
