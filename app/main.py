from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
from app.routes import  allocation

# Create FastAPI app instance
app = FastAPI()

# Routes
app.include_router(allocation.router, prefix="/allocations", tags=["allocations"])

# Swagger Docs
@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint of the Vehicle Allocation System API.

    - **Returns**: A simple welcome message as JSON, indicating that the API is running.
    - **Path**: `GET /`
    - **Swagger Tag**: "Root"

    This endpoint serves as a basic introduction to the API and can be used to check if the server is up.
    """
    return {"message": "Welcome to the Vehicle Allocation System"}
