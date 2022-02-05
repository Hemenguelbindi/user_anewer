from fastapi import FastAPI
from routes.search_by_value_in_db import search


app = FastAPI()
app.include_router(search)


@app.get('/')
async def root():
    return {"message": "Hello in api man!"}
