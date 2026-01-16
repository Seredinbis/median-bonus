from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api import business_router
from app.database.bootstrap import init_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_database()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(business_router)

if __name__ == "__main__":
    uvicorn.run(
        "app.__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
