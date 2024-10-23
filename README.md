# Vehicle Allocation System

## Overview
The Vehicle Allocation System is a web application built using FastAPI to manage the allocation of vehicles to employees. It allows you to create, update, delete, and fetch vehicle allocation records for employees. This project is containerized using Docker to ensure ease of deployment and consistent environment setup.

## Features
- Create new vehicle allocations for employees.
- Update existing allocations.
- Delete allocations.
- Fetch allocation history based on filters like employee ID, vehicle ID, and allocation date range.
- Integrated with MongoDB for data storage.

## Prerequisites
Before running the application, ensure you have the following installed:
- Docker
- Python 3.10 (if running locally without Docker)
- MongoDB (set up locally or with a cloud provider)

## Project Structure

## API Endpoints

### Allocation Endpoints
- **Create Allocation (POST /allocations/)**
  - **Request body:**
    ```json
    {
      "employee_id": 1,
      "vehicle_id": 101,
      "allocation_date": "2024-01-01"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Allocation created successfully"
    }
    ```

- **Update Allocation (PUT /allocations/{allocation_id})**
  - **Request body:**
    ```json
    {
      "vehicle_id": 102,
      "allocation_date": "2024-01-10"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Allocation updated successfully!"
    }
    ```

- **Delete Allocation (DELETE /allocations/{allocation_id})**
  - **Response:**
    ```json
    {
      "message": "Allocation deleted successfully!"
    }
    ```

### History Endpoints
- **Get Allocation History (GET /allocations/history/)**
  - **Query parameters (optional):** employee_id, vehicle_id, date_from, date_to
  - **Example request:** `/allocations/history/?employee_id=1&vehicle_id=101&date_from=2024-01-01&date_to=2024-01-31`
  - **Response:**
    ```json
    [
      {
        "id": "64bcfa5a...",
        "employee_id": 1,
        "vehicle_id": 101,
        "allocation_date": "2024-01-10"
      }
    ]
    ```

## Running the Application



### Using Docker
1. **Build the Docker Image**
   ```bash
   docker build -t vehicle_allocation .
2. Run Docker image
   ```
   docker run -p 8000:8000 vehicle_allocation

3. I used docker-compose.yml for that run this command .
   ```bash
     docker-compose up --build 
         

### Locally 
1. **Set Up Vertualenv** 
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate .

2. Install Dependencies
   ```bash
     pip install -r requirements.txt 

3. Run
   
  ```bash
    uvicorn app.main:app --reload


