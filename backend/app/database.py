from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

clinet = AsyncIOMotorClient(MONGODB_URL)
db = clinet[DB_NAME]

def get_database():
    return db

