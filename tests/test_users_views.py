
import json
from django.test import Client, RequestFactory
from users.views import add_user, list_users

def test_add_user_valid_request():
    client = Client()
    data = {'username': 'testuser', 'email': 'test@example.com'}
    response = client.post('/users/add/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.json() == {'message': 'User testuser created', 'email': 'test@example.com'}

def test_add_user_missing_username():
    client = Client()
    data = {'email': 'test@example.com'}
    response = client.post('/users/add/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing username'}

def test_add_user_invalid_json():
    client = Client()
    data = 'invalid json'
    response = client.post('/users/add/', data=data, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid JSON'}

def test_add_user_invalid_method():
    client = Client()
    response = client.get('/users/add/')
    assert response.status_code == 405
    assert response.json() == {'error': 'Invalid method'}

def test_list_users():
    client = Client()
    response = client.get('/users/list/')
    assert response.status_code == 200
    assert response.json() == {'users': ['user1', 'user2', 'user3']}

def test_list_users_invalid_method():
    client = Client()
    response = client.post('/users/list/')
    assert response.status_code == 405
    assert response.json() == {'error': 'Invalid method'}
