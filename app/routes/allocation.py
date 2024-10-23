from fastapi import APIRouter, HTTPException, Depends, Query
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import date, datetime
from bson import ObjectId
from app.dependencies import get_db

router = APIRouter()

class Allocation(BaseModel):
    employee_id: int
    vehicle_id: int
    allocation_date: date

    class Config:
        schema_extra = {
            "example": {
                "employee_id": 123,
                "vehicle_id": 456,
                "allocation_date": "2024-10-23",
            }
        }

@router.post("/", status_code=201, tags=["Allocations"])
async def create_allocation(allocation: Allocation, db=Depends(get_db)):
    """
    Create a new allocation for a vehicle to an employee.

    - **employee_id**: The ID of the employee.
    - **vehicle_id**: The ID of the vehicle.
    - **allocation_date**: The date when the vehicle is allocated.

    Raises a 400 error if:
    - The vehicle is already allocated on the given date.
    - The allocation date is in the past.
    """
    allocation_date_as_datetime = datetime.combine(allocation.allocation_date, datetime.min.time())

    existing_allocation = await db.allocations.find_one({
        "vehicle_id": allocation.vehicle_id,
        "allocation_date": allocation_date_as_datetime
    })

    if existing_allocation:
        raise HTTPException(status_code=400, detail="Vehicle is already allocated for this date.")

    if allocation.allocation_date < date.today():
        raise HTTPException(status_code=400, detail="Cannot allocate vehicle for a past date.")

    allocation_data = allocation.dict()
    allocation_data["allocation_date"] = allocation_date_as_datetime

    await db.allocations.insert_one(allocation_data)
    return {"message": "Allocation created successfully"}


@router.put("/{allocation_id}", tags=["Allocations"])
async def update_allocation(allocation_id: str, allocation: Allocation, db=Depends(get_db)):
    """
    Update an existing allocation by allocation ID.

    - **allocation_id**: The MongoDB ID of the allocation to update.
    - **employee_id**: The updated employee ID.
    - **vehicle_id**: The updated vehicle ID.
    - **allocation_date**: The updated allocation date.

    Raises a 404 error if the allocation is not found.
    Raises a 400 error if the allocation date is in the past.
    """
    current_allocation = await db.allocations.find_one({"_id": ObjectId(allocation_id)})

    if not current_allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")

    if current_allocation["allocation_date"] < date.today():
        raise HTTPException(status_code=400, detail="Cannot update allocation for a past date.")

    await db.allocations.update_one({"_id": ObjectId(allocation_id)}, {"$set": allocation.dict()})
    return {"message": "Allocation updated successfully!"}


@router.delete("/{allocation_id}", tags=["Allocations"])
async def delete_allocation(allocation_id: str, db=Depends(get_db)):
    """
    Delete an allocation by allocation ID.

    - **allocation_id**: The MongoDB ID of the allocation to delete.

    Raises a 404 error if the allocation is not found.
    Raises a 400 error if the allocation date is in the past.
    """
    allocation = await db.allocations.find_one({"_id": ObjectId(allocation_id)})

    if not allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")

    if allocation["allocation_date"] < date.today():
        raise HTTPException(status_code=400, detail="Cannot delete allocation for a past date.")

    await db.allocations.delete_one({"_id": ObjectId(allocation_id)})
    return {"message": "Allocation deleted successfully!"}


@router.get("/history/", tags=["Allocations"])
async def get_allocation_history(
    employee_id: int = Query(None, description="Filter by employee ID"),
    vehicle_id: int = Query(None, description="Filter by vehicle ID"),
    date_from: date = Query(None, description="Start date for the date range"),
    date_to: date = Query(None, description="End date for the date range"),
    db=Depends(get_db)
):
    """
    Retrieve the allocation history for a specific employee, vehicle, or date range.

    - **employee_id**: (Optional) Filter by employee ID.
    - **vehicle_id**: (Optional) Filter by vehicle ID.
    - **date_from**: (Optional) The start of the allocation date range.
    - **date_to**: (Optional) The end of the allocation date range.

    Returns a list of allocations matching the criteria.
    """
    query = {}

    if employee_id:
        query["employee_id"] = employee_id
    if vehicle_id:
        query["vehicle_id"] = vehicle_id
    if date_from and date_to:
        query["allocation_date"] = {"$gte": date_from, "$lte": date_to}

    allocations = await db.allocations.find(query).to_list(length=100)
    return allocations
