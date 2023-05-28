import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Content
from .serializers import UserSerializer, ContentSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def admin_user():
    return User.objects.create_user(username='admin', email='admin@example.com', password='admin123', role='admin')

@pytest.fixture
def author_user():
    return User.objects.create_user(username='author', email='author@example.com', password='author123', role='author')

@pytest.fixture
def content(admin_user):
    return Content.objects.create(user=admin_user, title='Test Content', body='Lorem ipsum...', summary='Summary', categories='Category')

def test_user_registration(api_client):
    url = reverse('user-register')
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword',
        'role': 'author'
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

def test_user_detail(api_client, admin_user):
    url = reverse('user-detail', kwargs={'pk': admin_user.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_content_list(api_client, admin_user):
    url = reverse('content-list')
    api_client.force_authenticate(user=admin_user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_content_detail(api_client, admin_user, content):
    url = reverse('content-detail', kwargs={'pk': content.id})
    api_client.force_authenticate(user=admin_user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_author_create_content(api_client, author_user):
    url = reverse('content-list')
    api_client.force_authenticate(user=author_user)
    data = {
        'user': author_user.id,
        'title': 'New Content',
        'body': 'Lorem ipsum...',
        'summary': 'Summary',
        'categories': 'Category'
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

def test_author_cannot_create_content_for_others(api_client, author_user):
    url = reverse('content-list')
    api_client.force_authenticate(user=author_user)
    data = {
        'user': author_user.id + 1,  # Trying to create content for another user
        'title': 'New Content',
        'body': 'Lorem ipsum...',
        'summary': 'Summary',
        'categories': 'Category'
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

# Add more tests as per your requirements




# ************************************
# Run the tests using the following command:


# pytest