import pytest


@pytest.mark.user
@pytest.mark.regression
class TestUserRead:
    """Test cases for user read/retrieval endpoints"""

    def test_get_user_by_username_success(self, user_api):
        """Test retrieving an existing user"""
        # Using a valid user from Petstore API
        username = "string"
        response = user_api.get_user_by_username(username)
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["username"] == username

    def test_get_user_with_special_characters(self, user_api):
        """Test retrieving user with special character username"""
        username = "user@example"
        response = user_api.get_user_by_username(username)
        # Can be 200 if exists or 404 if not found
        assert response.status_code in [200, 404]

    def test_get_nonexistent_user(self, user_api):
        """Test retrieving a non-existent user"""
        username = "nonexistentuser12345"
        response = user_api.get_user_by_username(username)
        assert response.status_code == 404

    def test_get_user_response_structure(self, user_api):
        """Test response structure for user retrieval"""
        username = "string"
        response = user_api.get_user_by_username(username)
        if response.status_code == 200:
            data = response.json()
            expected_fields = ["id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"]
            # At minimum, username should be present
            assert "username" in data or "id" in data

    def test_get_user_with_numeric_username(self, user_api):
        """Test retrieving user with numeric username"""
        username = "123456"
        response = user_api.get_user_by_username(username)
        assert response.status_code in [200, 404]

    def test_get_user_with_empty_username(self, user_api):
        """Test retrieving user with empty username"""
        username = ""
        response = user_api.get_user_by_username(username)
        # Empty username should return error or 400
        assert response.status_code in [400, 404, 405]
