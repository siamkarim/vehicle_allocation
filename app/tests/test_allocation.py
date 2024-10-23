from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_allocation():
    response = client.post("/allocations/", json={
        "employee_id": 1,
        "vehicle_id": 1,
        "allocation_date": "2024-12-01"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Allocation successful!"
