from motor.motor_asyncio import AsyncIOMotorClient
from config import Config
class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    async def close_connection(self):
        self.client.close()

    async def init_connection(self):
        await self.client.connect()
        await self.db

database = Database(
    uri=Config.MONGODB_URI,
    db_name=Config.MONGODB_NAME
)

async def close_mongo_connection():
    await database.close_connection()

async def init_mongo():
    await database.init_connection()

def get_db():
    return database.db

def get_collection(collection_name: str):
    return database.db[collection_name]
