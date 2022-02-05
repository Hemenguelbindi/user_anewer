from pydantic import BaseModel


class Man(BaseModel):
    name: str
    email: str
    age: int
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int
