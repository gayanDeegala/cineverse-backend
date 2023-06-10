from fastapi import FastAPI

from app.database.schema import create_schema

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/create_schema")
def run_create_schema():
    create_schema()
    return {"message": "Schema created successfully."}