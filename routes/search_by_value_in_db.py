from typing import List, Dict
from fastapi import APIRouter
from db.sampling_by_values import (
    retrieve_peoples_all,
    retrieve_peoples_one_by_name,
    retrieve_peoples_all_by_name,
    retrieve_peoples_one_by_age,
    retrieve_peoples_one_by_gender,
    retrieve_peoples_all_by_age,
    retrieve_peoples_all_by_gender,
    retrieve_peoples_one_by_company,
    retrieve_peoples_all_by_company,
    retrieve_peoples_all_by_email,
)
from models.man import Man

search = APIRouter()


# give all items in db
@search.get('/all')
async def give_all():
    return await retrieve_peoples_all()


# search by name
@search.get('/name_one_first/{name}')
async def find_one_by_from_name(name):
    return await retrieve_peoples_one_by_name(name)


@search.get('/{name}', response_model=List[Man])
async def find_all_by_from_name(name):
    return await retrieve_peoples_all_by_name(name)


# search by age
@search.get('/age_one_first/{age}')
async def find_one_by_from_age(age):
    return await retrieve_peoples_one_by_age(int(age))


@search.get('/age/{age}')
async def find_one_by_from_age(age):
    return await retrieve_peoples_all_by_age(int(age))


# search by gender
@search.get('/gender_one_any/{gender}')
async def find_one_by_from_gender(gender):
    return await retrieve_peoples_one_by_gender(gender)


@search.get('/gender/{gender}')
async def find_all_by_from_gender(gender):
    return await retrieve_peoples_all_by_gender(gender)

# search by company
@search.get('/company_one_any/{company}')
async def find_one_any_by_from_company(company):
    return await retrieve_peoples_one_by_company(company)


@search.get('/company/{company}', response_model=List[Man])
async def find_all_by_from_company(company):
    return await retrieve_peoples_all_by_company(company)


# search by email
@search.get('/email/{email}')
async def find_all_by_from_email(email):
    return await retrieve_peoples_all_by_email(email)
