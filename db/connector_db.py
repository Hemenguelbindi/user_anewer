from motor.motor_asyncio import AsyncIOMotorClient
from config.env import mongo_conn, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from loguru import logger

logger.add("test_connect.db")

conn = AsyncIOMotorClient(mongo_conn)
db = conn.people_db
people_coll = db.get_collection("all")


async def connect_to_mongo():
    logger.info("Connect in data base")
    db.client = AsyncIOMotorClient(str(conn),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logger.info("Successfully connected to the database!")


async def close_mongo_connection():
    logger.info("Close the database connection.  .  .")
    db.client.close()
    logger.info("The database connection is closed!")