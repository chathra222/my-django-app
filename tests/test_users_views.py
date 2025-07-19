import json
from django.test import Client, RequestFactory
from django.urls import reverse
from users.views import add_user, update_user, list_users

class TestUsersViews:
    def test_add_user_success(self):
        client = Client()
        data = {"username": "testuser", "email": "test@example.com"}
        response = client.post(reverse("add_user"), data=json.dumps(data), content_type="application/json")
        assert response.status_code == 201
        assert response.json() == {"message": "User testuser created", "email": "test@example.com"}

    def test_add_user_missing_username(self):
        client = Client()
        data = {"email": "test@example.com"}
        response = client.post(reverse("add_user"), data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400
        assert response.json() == {"error": "Missing username"}

    def test_add_user_missing_email(self):
        client = Client()
        data = {"username": "testuser"}
        response = client.post(reverse("add_user"), data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400
        assert response.json() == {"error": "Missing username or email"}

    def test_add_user_invalid_json(self):
        client = Client()
        response = client.post(reverse("add_user"), data="invalid json", content_type="application/json")
        assert response.status_code == 400
        assert response.json() == {"error": "Invalid JSON"}

    def test_update_user_success(self):
        client = Client()
        data = {"email": "new@example.com"}
        response = client.put(reverse("update_user", args=["testuser"]), data=json.dumps(data), content_type="application/json")
        assert response.status_code == 200
        assert response.json() == {"message": "User testuser updated", "email": "new@example.com"}

    def test_update_user_missing_email(self):
        client = Client()
        data = {}
        response = client.put(reverse("update_user", args=["testuser"]), data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400
        assert response.json() == {"error": "Missing email"}

    def test_update_user_invalid_json(self):
        client = Client()
        response = client.put(reverse("update_user", args=["testuser"]), data="invalid json", content_type="application/json")
        assert response.status_code == 400
        assert response.json() == {"error": "Invalid JSON"}

    def test_list_users_success(self):
        client = Client()
        response = client.get(reverse("list_users"))
        assert response.status_code == 200
        assert response.json() == {"users": ["user1", "user2", "user3"]}

    def test_list_users_invalid_method(self):
        client = Client()
        response = client.post(reverse("list_users"))
        assert response.status_code == 405
        assert response.json() == {"error": "Invalid method"}