
# Test cases for users/views.py

import json
from django.test import Client, RequestFactory
from django.urls import reverse
from .views import add_user, update_user, list_users

def test_add_user_valid_request():
    client = Client()
    data = {'username': 'testuser', 'email': 'test@example.com'}
    response = client.post(reverse('add_user'), data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.json() == {'message': 'User testuser created', 'email': 'test@example.com'}

def test_add_user_missing_username():
    client = Client()
    data = {'email': 'test@example.com'}
    response = client.post(reverse('add_user'), data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing username'}

def test_add_user_invalid_json():
    client = Client()
    data = 'invalid json'
    response = client.post(reverse('add_user'), data=data, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid JSON'}

def test_add_user_invalid_method():
    client = Client()
    response = client.get(reverse('add_user'))
    assert response.status_code == 405
    assert response.json() == {'error': 'Invalid method'}

def test_update_user_valid_request():
    client = Client()
    data = {'email': 'new@example.com'}
    response = client.put(reverse('update_user', args=['testuser']), data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.json() == {'message': 'User testuser updated', 'email': 'new@example.com'}

def test_update_user_missing_email():
    client = Client()
    data = {}
    response = client.put(reverse('update_user', args=['testuser']), data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing email'}

def test_update_user_invalid_json():
    client = Client()
    data = 'invalid json'
    response = client.put(reverse('update_user', args=['testuser']), data=data, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid JSON'}

def test_update_user_invalid_method():
    client = Client()
    response = client.get(reverse('update_user', args=['testuser']))
    assert response.status_code == 405
    assert response.json() == {'error': 'Invalid method'}

def test_list_users_valid_request():
    client = Client()
    response = client.get(reverse('list_users'))
    assert response.status_code == 200
    assert response.json() == {'users': ['user1', 'user2', 'user3']}

def test_list_users_invalid_method():
    client = Client()
    response = client.post(reverse('list_users'))
    assert response.status_code == 405
    assert response.json() == {'error': 'Invalid method'}
