from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

# database class to initialize the connection to the database
class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri, uuidRepresentation="standard")
        self.db = self.client.get_database(db_name)

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

def get_collection():
    return database.db.get_collection("users")

