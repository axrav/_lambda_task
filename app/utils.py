from motor.motor_asyncio import AsyncIOMotorClient
from app.db import get_db

async def get_collection():
    db = get_db()
    return db["users"]
