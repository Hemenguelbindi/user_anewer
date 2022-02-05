from fastapi import APIRouter
from config.connector_db import conn
from schemas.user import users_entity
from loguru import logger

logger.add("router_user.log")

user = APIRouter()


@user.get('/{name}')
async def find_all_form_name(name):
    logger.info(conn.server_info())
    logger.info(conn.people_db.all.find({"name": name}))
    return users_entity(conn.people_db.all.find({"name": name}))
