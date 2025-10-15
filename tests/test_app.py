import pytest
from fastapi.testclient import TestClient
from app.app import app

# --- MOCK REDIS ---
class FakeRedis:
    def incr(self, key):
        return 1

import app.app as app_module
app_module.redis = FakeRedis()  # override redis with fake object for tests

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
