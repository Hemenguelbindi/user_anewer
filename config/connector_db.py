from pymongo import MongoClient
from .env import mongo_conn

conn = MongoClient(mongo_conn)


