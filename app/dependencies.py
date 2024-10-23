from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends

# Create MongoDB client
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["vehicle_allocation"]

def get_db():
    """
    Dependency function to get a reference to the MongoDB database.

    - **db**: Returns a reference to the `vehicle_allocation` database.
    - This function is designed to be used with FastAPI's `Depends` for injecting the database
      connection into route handlers.

    The `try-finally` block ensures that the database connection is properly closed
    after use when FastAPI finishes the request.

    **Yields**: 
        - The `db` object, which represents the MongoDB `vehicle_allocation` database.
    """
    try:
        yield db
    finally:
        client.close()
