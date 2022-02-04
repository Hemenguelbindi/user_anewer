from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    age: int
    company: str
    job_title: str
    gender: str
    salary: int