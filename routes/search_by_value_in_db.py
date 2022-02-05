from fastapi import APIRouter
from db.sampling_by_values import (
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

search = APIRouter()


# search by name
@search.get('/name_one_first/{name}')
async def find_one_by_from_name(name):
    people = await retrieve_peoples_one_by_name(name)
    return people


@search.get('/{name}')
async def find_all_by_from_name(name):
    people = await retrieve_peoples_all_by_name(name)
    return people


# search by age
@search.get('/age_one_first/{age}')
async def find_one_by_from_age(age):
    people = await retrieve_peoples_one_by_age(int(age))
    return people


@search.get('/age/{age}')
async def find_one_by_from_age(age):
    people = await retrieve_peoples_all_by_age(int(age))
    return people


# search by gender
@search.get('/gender_one_any/{gender}')
async def find_one_by_from_gender(gender):
    people = await retrieve_peoples_one_by_gender(gender)
    return people


@search.get('/gender/{gender}')
async def find_all_by_from_gender(gender):
    people = await retrieve_peoples_all_by_gender(gender)
    return people


# search by company
@search.get('/company_one_any/{company}')
async def find_one_any_by_from_company(company):
    people = await retrieve_peoples_one_by_company(company)
    return people


@search.get('/company/{company}')
async def find_all_by_from_company(company):
    people = await retrieve_peoples_all_by_company(company)
    return people


# search by email
@search.get('/email/{email}')
async def find_all_by_from_email(email):
    people = await retrieve_peoples_all_by_email(email)
    return people
