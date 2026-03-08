import pytest


@pytest.mark.user
@pytest.mark.regression
class TestUserDelete:
    """Test cases for user deletion endpoints"""

    def test_delete_user_success(self, user_api):
        """Test deleting an existing user"""
        username = "string"
        response = user_api.delete_user(username)
        assert response.status_code == 200

    def test_delete_nonexistent_user(self, user_api):
        """Test deleting a non-existent user"""
        username = "nonexistentuser12345"
        response = user_api.delete_user(username)
        # May return 404 or 200 depending on API behavior (idempotent)
        assert response.status_code in [200, 404]

    
    def test_delete_user_response_structure(self, user_api):
        """Test response structure when deleting user"""
        username = "testdeleteuser"
        response = user_api.delete_user(username)
        if response.status_code == 200:
            # Response should be valid JSON or empty
            try:
                data = response.json()
                assert "code" in data or len(data) == 0
            except ValueError:
                # Empty response is acceptable
                pass

    def test_delete_user_with_empty_username(self, user_api):
        """Test deleting user with empty username"""
        username = ""
        response = user_api.delete_user(username)
        # Empty username should return error or 400
        assert response.status_code in [400, 404, 405]
