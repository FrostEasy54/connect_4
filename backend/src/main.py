from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.views import router as api_router
from .connect_4.settings import settings
from .db.utils import get_mongodb_client


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # set up mongo DB
    client = get_mongodb_client()
    db = client.get_database(settings.MONGO_DB_DB)
    app.mongodb = db  # type: ignore [attr-defined]
    yield
    # close MongoDB connection
    client.close()  # type: ignore [attr-defined, operator]


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"hello": "sevtony world"}
