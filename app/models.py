from pydantic import BaseModel
from typing import List
from datetime import date

class Employee(BaseModel):
    """
    Represents an employee in the vehicle allocation system.

    - **id** (int): Unique identifier for the employee.
    - **name** (str): The employee's full name.
    - **department** (str): The department the employee belongs to.
    """
    id: int
    name: str
    department: str

class Vehicle(BaseModel):
    """
    Represents a vehicle in the vehicle allocation system.

    - **id** (int): Unique identifier for the vehicle.
    - **model** (str): Model of the vehicle.
    - **driver_id** (int): ID of the driver assigned to the vehicle.
    """
    id: int
    model: str
    driver_id: int

class Allocation(BaseModel):
    """
    Represents a vehicle allocation to an employee.

    - **employee_id** (int): ID of the employee to whom the vehicle is allocated.
    - **vehicle_id** (int): ID of the allocated vehicle.
    - **date** (date): The date on which the vehicle is allocated.
    """
    employee_id: int
    vehicle_id: int
    date: date

class AllocationUpdate(BaseModel):
    """
    Represents the data required to update an existing vehicle allocation.

    - **vehicle_id** (int): ID of the new vehicle being allocated.
    - **date** (date): The new date for the vehicle allocation.
    """
    vehicle_id: int
    date: date
