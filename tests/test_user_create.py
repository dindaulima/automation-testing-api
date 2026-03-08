import pytest


@pytest.mark.user
@pytest.mark.smoke
class TestUserCreate:
    """Test cases for user creation endpoints"""

    def test_create_user_success(self, user_api, sample_user):
        """Test creating a user successfully"""
        response = user_api.create_user(sample_user)
        assert response.status_code == 200
        data = response.json()
        assert "code" in data
        assert data["code"] == 200

    def test_create_user_with_minimal_data(self, user_api):
        """Test creating a user with minimal required data"""
        minimal_user = {
            "username": "minimaluser"
        }
        response = user_api.create_user(minimal_user)
        assert response.status_code == 200

    def test_create_multiple_users(self, user_api, sample_users):
        """Test creating multiple users with list endpoint"""
        response = user_api.create_users_with_list(sample_users)
        assert response.status_code == 200
        data = response.json()
        assert "code" in data
        assert data["code"] == 200

    def test_create_user_with_long_string(self, user_api):
        """Test creating a user with long string values"""
        user = {
            "username": "longnameuser",
            "firstName": "A" * 100,
            "lastName": "B" * 100,
            "email": "long@example.com"
        }
        response = user_api.create_user(user)
        assert response.status_code == 200
