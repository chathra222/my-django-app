# tests/test_users.py
import pytest
import json
from django.test import Client
from django.urls import reverse

# @pytest.mark.django_db
# def test_add_user(client):
#     url = "/api/add-user/"
#     payload = {
#         "username": "johndoe",
#         "email": "john@example.com"
#     }
#     response = client.post(url, data=json.dumps(payload), content_type="application/json")

#     assert response.status_code == 201
#     assert response.json()["message"] == "User johndoe created"
#     assert response.json()["email"] == "john@example.com"

# @pytest.mark.django_db
# #write test for list users
# def test_list_users(client):
#     url = "/api/list-users/"
#     response = client.get(url)

#     assert response.status_code == 200
#     assert "users" in response.json()
#     assert isinstance(response.json()["users"], list)
#     assert len(response.json()["users"]) > 0

@pytest.mark.django_db
def test_add_user_valid_request():
    client = Client()
    data = {"username": "testuser", "email": "test@example.com"}
    response = client.post(reverse("add_user"), data=json.dumps(data), content_type="application/json")
    assert response.status_code == 201
    assert response.json() == {"message": "User testuser created", "email": "test@example.com"}

@pytest.mark.django_db  
def test_add_user_missing_username():
    client = Client()
    data = {"email": "test@example.com"}
    response = client.post(reverse("add_user"), data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400
    assert response.json() == {"error": "Missing username"}

@pytest.mark.django_db
def test_add_user_missing_username_and_email():
    client = Client()
    data = {}
    response = client.post(reverse("add_user"), data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400
    assert response.json() == {"error": "Missing username or email"}

@pytest.mark.django_db
def test_add_user_invalid_json():
    client = Client()
    data = "invalid json"
    response = client.post(reverse("add_user"), data=data, content_type="application/json")
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid JSON"}

@pytest.mark.django_db
def test_add_user_invalid_method():
    client = Client()
    response = client.get(reverse("add_user"))
    assert response.status_code == 405
    assert response.json() == {"error": "Invalid method"}

@pytest.mark.django_db
def test_list_users_valid_request():
    client = Client()
    response = client.get(reverse("list_users"))
    assert response.status_code == 200
    assert response.json() == {"users": ["user1", "user2", "user3"]}

@pytest.mark.django_db
def test_list_users_invalid_method():
    client = Client()
    response = client.post(reverse("list_users"))
    assert response.status_code == 405
    assert response.json() == {"error": "Invalid method"}
