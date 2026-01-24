# ruff: noqa: F401
# noinspection PyUnresolvedReferences
from app.domain.base import Entity

# noinspection PyUnresolvedReferences
from app.domain.bonus import Bonus, BonusType

# noinspection PyUnresolvedReferences
from app.domain.business import Business, BusinessStatus

# noinspection PyUnresolvedReferences
from app.domain.customer import Customer, CustomerStatus

# noinspection PyUnresolvedReferences
from app.domain.order import Order, OrderStatus

# noinspection PyUnresolvedReferences
from app.domain.product import Product, ProductStatus

# noinspection PyUnresolvedReferences
from app.domain.store import Store, StoreStatus

from .session import engine


async def init_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Entity.metadata.create_all)


# for early dev purposes only
async def drop_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Entity.metadata.drop_all)
