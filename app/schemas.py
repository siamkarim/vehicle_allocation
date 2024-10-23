from pydantic import BaseModel
from datetime import date
from typing import Optional


class AllocationCreateSchema(BaseModel):
    """
    Schema for creating a new vehicle allocation.

    - **employee_id** (int): ID of the employee receiving the vehicle allocation.
    - **vehicle_id** (int): ID of the vehicle being allocated.
    - **allocation_date** (date): The date on which the vehicle is allocated to the employee.

    This schema is used when a new allocation is being created in the system.
    """
    employee_id: int
    vehicle_id: int
    allocation_date: date


class AllocationUpdateSchema(BaseModel):
    """
    Schema for updating an existing vehicle allocation.

    - **vehicle_id** (int): ID of the new or updated vehicle being allocated.
    - **allocation_date** (date): The updated date of the vehicle allocation.

    This schema is used when updating an existing allocation, such as modifying the vehicle or date.
    """
    vehicle_id: int
    allocation_date: date


class AllocationReadSchema(BaseModel):
    """
    Schema for reading an allocation, typically used when fetching allocation data (e.g., in reports).

    - **id** (str): Unique identifier for the allocation (usually the MongoDB ObjectId as a string).
    - **employee_id** (int): ID of the employee associated with the allocation.
    - **vehicle_id** (int): ID of the vehicle that was allocated.
    - **allocation_date** (date): The date the allocation took place.

    This schema is useful for displaying or returning allocation data, such as in history reports or read operations.
    """
    id: str
    employee_id: int
    vehicle_id: int
    allocation_date: date

