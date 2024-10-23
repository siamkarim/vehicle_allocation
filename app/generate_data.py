from motor.motor_asyncio import AsyncIOMotorClient
from faker import Faker
import asyncio

fake = Faker()

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "vehicle_allocation"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

async def create_employees_and_vehicles():
    employees = []
    vehicles = []
    for i in range(1, 1001):
        # Generate Employee
        employee = {
            "id": i,
            "name": fake.name(),
            "department": fake.company()
        }
        employees.append(employee)
        
        # Generate Vehicle
        vehicle = {
            "id": i,
            "model": fake.company() + " " + fake.word(),
            "driver_id": i
        }
        vehicles.append(vehicle)

    # Insert into MongoDB
    await db.employees.insert_many(employees)
    await db.vehicles.insert_many(vehicles)
    print(f"Inserted {len(employees)} employees and {len(vehicles)} vehicles.")

async def main():
    await create_employees_and_vehicles()
    client.close()

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
