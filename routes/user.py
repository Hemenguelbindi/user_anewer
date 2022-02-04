from fastapi import APIRouter

from models.user import User
from config.connector_db import conn
from schemas.user import user_entity, users_entity
from loguru import logger

logger.add("router_user.log")

user = APIRouter()


@user.get('/{name}')
async def find_all_name(name):
    logger.info(conn.server_info())
    logger.info(conn.people_db.all.find({"name": name}))
    return users_entity(conn.people_db.all.find({"name": name}))


@user.get('/{company}')
async def find_all_company(company):
    logger.info(conn.server_info())
    logger.info(conn.people_db.all.find({"job_title": company}))
    return users_entity(conn.people_db.all.find({"job_title": company}))


@user.post('/')
async def create_user(user_: User):
    conn.local.user.insert_one(dict(user_))
    return users_entity(conn.local.user.find())
