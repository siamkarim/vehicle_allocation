from datetime import date
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models import Allocation

async def create_allocation(db: AsyncIOMotorDatabase, allocation: Allocation):
    """
    Create a new vehicle allocation in the database.

    - **db**: The MongoDB database instance.
    - **allocation**: The allocation data to be inserted, provided as an instance of the `Allocation` model.

    Inserts the allocation data into the `allocations` collection.
    """
    allocation_data = allocation.dict()
    await db.allocations.insert_one(allocation_data)

async def update_allocation(db: AsyncIOMotorDatabase, allocation_id: str, allocation: Allocation):
    """
    Update an existing allocation in the database.

    - **db**: The MongoDB database instance.
    - **allocation_id**: The ID of the allocation to update.
    - **allocation**: The updated allocation data provided as an instance of the `Allocation` model.

    Updates the allocation in the `allocations` collection based on the provided allocation ID.
    """
    await db.allocations.update_one({"_id": allocation_id}, {"$set": allocation.dict()})

async def delete_allocation(db: AsyncIOMotorDatabase, allocation_id: str):
    """
    Delete an allocation from the database.

    - **db**: The MongoDB database instance.
    - **allocation_id**: The ID of the allocation to delete.

    Deletes the specified allocation from the `allocations` collection.
    """
    await db.allocations.delete_one({"_id": allocation_id})

async def check_allocation_exists(db: AsyncIOMotorDatabase, vehicle_id: int, date: date):
    """
    Check if a vehicle is already allocated on a given date.

    - **db**: The MongoDB database instance.
    - **vehicle_id**: The ID of the vehicle to check.
    - **date**: The date for which to check the allocation.

    Returns `True` if an allocation exists for the given vehicle and date, otherwise returns `False`.
    """
    allocation = await db.allocations.find_one({"vehicle_id": vehicle_id, "date": date})
    return allocation is not None

async def get_history_report(filters: dict):
    """
    Generate a history report based on the provided filters.

    - **filters**: A dictionary containing filtering options such as employee ID, vehicle ID, and date range.

    Processes the filters and returns the history report. 
    Implementation needs to be added for this function.
    """
    pass
