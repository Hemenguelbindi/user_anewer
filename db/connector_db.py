from motor.motor_asyncio import AsyncIOMotorClient
from config.env import mongo_conn


conn = AsyncIOMotorClient(mongo_conn)
db = conn.people_db
people_coll = db.get_collection("all")


