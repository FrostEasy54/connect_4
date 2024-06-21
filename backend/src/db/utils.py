from motor.motor_asyncio import AsyncIOMotorClient

from ..connect_4.settings import settings


def get_mongodb_client() -> AsyncIOMotorClient:
    """get MongoDB client instance"""
    return AsyncIOMotorClient(settings.MONGO_DB_URL)
