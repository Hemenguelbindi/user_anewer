from fastapi import FastAPI
from routes.user import user

app = FastAPI()
app.include_router(user)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
