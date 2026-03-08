import pytest


@pytest.mark.user
@pytest.mark.regression
class TestUserUpdate:
    """Test cases for user update endpoints"""

    def test_update_user_success(self, user_api):
        """Test updating an existing user"""
        username = "string"
        updated_data = {
            "username": "string",
            "firstName": "Updated",
            "lastName": "Name",
            "email": "updated@example.com",
            "password": "newpassword",
            "phone": "9999999999",
            "userStatus": 1
        }
        response = user_api.update_user(username, updated_data)
        assert response.status_code == 200

    def test_update_user_partial(self, user_api):
        """Test updating user with partial data"""
        username = "string"
        partial_data = {
            "firstName": "PartialUpdate",
            "email": "partial@example.com"
        }
        response = user_api.update_user(username, partial_data)
        assert response.status_code == 200

    def test_update_nonexistent_user(self, user_api):
        """Test updating a non-existent user"""
        username = "nonexistentuser12345"
        update_data = {
            "firstName": "Test"
        }
        response = user_api.update_user(username, update_data)
        # May return 404 or 200 depending on API behavior
        assert response.status_code in [200, 404]

    def test_update_user_email_field(self, user_api):
        """Test updating only the email field"""
        username = "string"
        update_data = {
            "email": "newemail@example.com"
        }
        response = user_api.update_user(username, update_data)
        assert response.status_code == 200

    def test_update_user_empty_body(self, user_api):
        """Test updating user with empty body"""
        username = "string"
        response = user_api.update_user(username, {})
        assert response.status_code == 200
