from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    name: str
    email: str
    age: int
    company: str
    join_date: date
    job_title: str
    gender: str
    salary: int

    class Congig:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True