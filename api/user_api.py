import requests
from config.settings import BASE_URL, TIMEOUT


class UserAPI:
    """API client for User endpoints in Petstore API"""

    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
        self.endpoint = "/user"

    def create_user(self, user_data):
        """Create a new user"""
        url = f"{self.base_url}{self.endpoint}"
        return requests.post(url, json=user_data, timeout=self.timeout)

    def create_users_with_list(self, users_data):
        """Create multiple users with a list"""
        url = f"{self.base_url}{self.endpoint}/createWithList"
        return requests.post(url, json=users_data, timeout=self.timeout)

    def get_user_by_username(self, username):
        """Get user by username"""
        url = f"{self.base_url}{self.endpoint}/{username}"
        return requests.get(url, timeout=self.timeout)

    def update_user(self, username, user_data):
        """Update user information"""
        url = f"{self.base_url}{self.endpoint}/{username}"
        return requests.put(url, json=user_data, timeout=self.timeout)

    def delete_user(self, username):
        """Delete a user"""
        url = f"{self.base_url}{self.endpoint}/{username}"
        return requests.delete(url, timeout=self.timeout)

    def login_user(self, username, password):
        """Login user"""
        url = f"{self.base_url}{self.endpoint}/login"
        params = {"username": username, "password": password}
        return requests.get(url, params=params, timeout=self.timeout)

    def logout_user(self):
        """Logout user"""
        url = f"{self.base_url}{self.endpoint}/logout"
        return requests.get(url, timeout=self.timeout)
