from db.connector_db import people_coll
from schemas.user import people_entity
from loguru import logger

logger.add("log_db.log")


# search all data
async def retrieve_peoples_all():
    people = []
    async for p in people_coll.find():
        people.append(p)
    return people


# search by first match
async def retrieve_peoples_one_by_name(name: str) -> dict:
    items = await people_coll.find_one({"name": name})
    logger.info("Get item db:", items)
    if items:
        return people_entity(items)


async def retrieve_peoples_one_by_age(age: str) -> dict:
    items = await people_coll.find_one({"age": age})
    logger.info("Get item db:", items)
    if items:
        return people_entity(items)


async def retrieve_peoples_one_by_gender(gender: str) -> dict:
    result = await people_coll.find_one({"gender": gender})
    logger.info("Get item db:", result)
    if result:
        return people_entity(result)


async def retrieve_peoples_one_by_company(company: str) -> dict:
    result = await people_coll.find_one({"company": company})
    logger.info("Get item db:", result)
    if result:
        return people_entity(result)


# search for all suitable
async def retrieve_peoples_all_by_name(name: str) -> list[dict]:
    result = []
    async for doc in people_coll.find({"name": name}):
        result.append(people_entity(doc))
    logger.info("Get item db:", result)
    return result


async def retrieve_peoples_all_by_age(age: str) -> list[dict]:
    result = []
    async for doc in people_coll.find({"age": age}):
        result.append(people_entity(doc))
    logger.info("Get item db:", result)
    return result


async def retrieve_peoples_all_by_gender(gender: str) -> list[dict]:
    result = []
    async for doc in people_coll.find({"gender": gender}):
        result.append(people_entity(doc))
    logger.info("Get item db:", result)
    return result


async def retrieve_peoples_all_by_company(company: str) -> list[dict]:
    result = []
    async for doc in people_coll.find({"company": company}):
        result.append(people_entity(doc))
    logger.info("Get item db:", result)
    return result


async def retrieve_peoples_all_by_email(company: str) -> list[dict]:
    result = []
    async for doc in people_coll.find({"company": company}):
        result.append(people_entity(doc))
    logger.info("Get item db:", result)
    return result
