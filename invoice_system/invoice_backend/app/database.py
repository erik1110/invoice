from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.media import Media
from app.models.data import Data
import os

async def initiate_database():
    mongo_uri = os.environ["MONGO_URI"]
    client = AsyncIOMotorClient(mongo_uri)
    await init_beanie(database=client.get_default_database(),
                      document_models=[Data, Media])
