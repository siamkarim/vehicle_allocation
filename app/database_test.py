import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def test_connection():
    """
    Test the connection to the MongoDB server and print the server status.

    - Connects to MongoDB using `AsyncIOMotorClient` at the default `localhost:27017` address.
    - Accesses the `vehicle_allocation` database.
    - Sends a `serverStatus` command to MongoDB, which returns statistics and server status metrics.
    - Prints the result to the console.
    """
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.vehicle_allocation
    print(await db.command("serverStatus"))

if __name__ == "__main__":
    """
    Entry point of the script.
    Uses asyncio to run the `test_connection` coroutine.
    """
    asyncio.run(test_connection())
