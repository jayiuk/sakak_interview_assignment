from fastapi.testclient import TestClient
from service.api.MockAPI import router

def test_mock_api(patientId = 1):
    with TestClient(router) as client:
        response = client.get("/api/health/{patientId}")
        
        assert response.status_code == 200
        result = response.json()
        print(result)