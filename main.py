from fastapi import FastAPI
from routes.search_by_value_in_db import search

app = FastAPI()
app.include_router(search)
