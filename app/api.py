from fastapi import FastAPI
from app.infrastructure.models.base import Base
from app.infrastructure.database.fx_database import engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.infrastructure.models import user
    # Startup: create tables
    import logging
    logging.basicConfig(level=logging.INFO)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logging.info("Tables created")
    yield


app = FastAPI(
    title="FX Wallet API",
    description="A simple API to manage a multi-currency wallet with real-time exchange rates.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/ping/", tags=["Health Check"])
async def ping():
    return {"message": "pong"}
