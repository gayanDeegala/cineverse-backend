from fastapi import FastAPI

from app.database.schema import create_schema
from app.routers.booking import router as booking_router
from app.routers.events import router as event_router

app = FastAPI()

# Include the booking router
app.include_router(booking_router)

# Include the event router
app.include_router(event_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/create_schema")
def run_create_schema():
    create_schema()
    return {"message": "Schema created successfully."}