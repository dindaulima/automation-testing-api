import pytest
from api.user_api import UserAPI


@pytest.fixture
def user_api():
    """Fixture for UserAPI client"""
    return UserAPI()


@pytest.fixture
def sample_user():
    """Fixture for sample user data"""
    return {
        "username": "testuser123",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }


@pytest.fixture
def sample_users():
    """Fixture for multiple users"""
    return [
        {
            "username": "user1",
            "firstName": "John",
            "lastName": "Doe",
            "email": "john@example.com",
            "password": "pass123",
            "phone": "1111111111",
            "userStatus": 1
        },
        {
           "username": "user2",
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "jane@example.com",
            "password": "pass456",
            "phone": "2222222222",
            "userStatus": 1
        }
    ]
