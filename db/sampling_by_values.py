import asyncio
from db.connector_db import people_coll
from schemas.user import people_entity
from loguru import logger

logger.add("log_db.log")


# search all data
async def retrieve_peoples_all():
    logger.info("Search all")
    return list(p async for p in people_coll.find())


# search by first match
async def retrieve_peoples_one_by_name(name: str) -> dict:
    logger.info("Search one by name:", name)
    if await people_coll.find_one({"name": name}):
        return people_entity(await people_coll.find_one({"name": name}))


async def retrieve_peoples_one_by_age(age: str) -> dict:
    logger.info("Search one by age:", age)
    if await people_coll.find_one({"age": age}):
        return people_entity(await people_coll.find_one({"age": age}))


async def retrieve_peoples_one_by_gender(gender: str) -> dict:
    logger.info("Search one by gender:", gender)
    if await people_coll.find_one({"gender": gender}):
        return people_entity(await people_coll.find_one({"gender": gender}))


async def retrieve_peoples_one_by_company(company: str) -> dict:
    logger.info("Seasrch one by company:", company)
    if await people_coll.find_one({"company": company}):
        return people_entity(await people_coll.find_one({"company": company}))


# search for all suitable
async def retrieve_peoples_all_by_name(name: str) -> list[dict]:
    logger.info("Search by name:", name)
    return list(doc async for doc in people_coll.find({"name": name}))


async def retrieve_peoples_all_by_age(age: str) -> list[dict]:
    logger.info("Search by age:", age)
    return list(doc async for doc in people_coll.find({"age": age}))


async def retrieve_peoples_all_by_gender(gender: str) -> list[dict]:
    logger.info("Search by gender:", gender)
    return list(doc async for doc in people_coll.find({"gender": gender}))


async def retrieve_peoples_all_by_company(company: str) -> list[dict]:
    logger.info("Search by company:", company)
    return list(doc async for doc in people_coll.find({"company": company}))


async def retrieve_peoples_all_by_email(email_: str) -> list[dict]:
    logger.info("Search by email", email_)
    return list(doc async for doc in people_coll.find({"email": email_}))
