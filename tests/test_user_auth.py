import pytest


@pytest.mark.user
@pytest.mark.smoke
class TestUserAuth:
    """Test cases for user authentication endpoints"""

    def test_login_user_success(self, user_api):
        """Test successful user login"""
        response = user_api.login_user("user1", "Password1!")
        assert response.status_code == 200
        data = response.json()
        assert "code" in data
        assert data["code"] == 200

    def test_login_with_invalid_credentials(self, user_api):
        """Test login with invalid credentials"""
        response = user_api.login_user("invaliduser", "wrongpassword")
        # Should return 400 for invalid credentials
        assert response.status_code in [400, 401, 404]

    def test_login_with_empty_username(self, user_api):
        """Test login with empty username"""
        response = user_api.login_user("", "password")
        assert response.status_code in [400, 401, 404]

    def test_login_with_empty_password(self, user_api):
        """Test login with empty password"""
        response = user_api.login_user("testuser", "")
        assert response.status_code in [400, 401, 404]

    def test_logout_user(self, user_api):
        """Test user logout"""
        response = user_api.logout_user()
        assert response.status_code == 200
        data = response.json()
        assert "code" in data
        assert data["code"] == 200
