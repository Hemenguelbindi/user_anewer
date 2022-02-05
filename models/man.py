from pydantic import BaseModel
from datetime import date


class Man(BaseModel):
    name: str
    email: str
    age: int
    company: str
    join_date: date
    job_title: str
    gender: str
    salary: int
