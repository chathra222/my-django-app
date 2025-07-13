# tests/test_users.py
import pytest
import json

@pytest.mark.django_db
def test_add_user(client):
    url = "/api/add-user/"
    payload = {
        "username": "johndoe",
        "email": "john@example.com"
    }
    response = client.post(url, data=json.dumps(payload), content_type="application/json")

    assert response.status_code == 201
    assert response.json()["message"] == "User johndoe created"
    assert response.json()["email"] == "john@example.com"

@pytest.mark.django_db
#write test for list users
def test_list_users(client):
    url = "/api/list-users/"
    response = client.get(url)

    assert response.status_code == 200
    assert "users" in response.json()
    assert isinstance(response.json()["users"], list)
    assert len(response.json()["users"]) > 0