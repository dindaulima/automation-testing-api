import pytest


@pytest.mark.pet
@pytest.mark.regression
class TestPetDelete:
    """Test cases for pet deletion endpoints"""

    def test_delete_pet_success(self, pet_api):
        """Test deleting an existing pet"""
        pet_id = 100
        response = pet_api.delete_pet(pet_id)
        assert response.status_code == 200

    def test_delete_nonexistent_pet(self, pet_api):
        """Test deleting a non-existent pet"""
        pet_id = 99999999
        response = pet_api.delete_pet(pet_id)
        # May return 404 or 200 (idempotent)
        assert response.status_code in [200, 404]

    def test_delete_pet_response_structure(self, pet_api):
        """Test response structure when deleting pet"""
        pet_id = 101
        response = pet_api.delete_pet(pet_id)
        if response.status_code == 200:
            try:
                data = response.json()
                assert "code" in data or len(data) == 0
            except ValueError:
                # Empty response is acceptable
                pass

    def test_delete_pet_with_invalid_id(self, pet_api):
        """Test deleting pet with invalid ID format"""
        pet_id = "invalid"
        response = pet_api.delete_pet(pet_id)
        assert response.status_code in [400, 404, 405]

    def test_delete_pet_twice(self, pet_api):
        """Test deleting the same pet twice"""
        pet_id = 102
        response1 = pet_api.delete_pet(pet_id)
        response2 = pet_api.delete_pet(pet_id)
        # First deletion should succeed, second may be 404
        assert response1.status_code in [200, 404]
        assert response2.status_code in [200, 404]

    def test_delete_pet_with_numeric_id(self, pet_api):
        """Test deleting pet with numeric ID"""
        pet_id = 12345
        response = pet_api.delete_pet(pet_id)
        assert response.status_code in [200, 404]

    def test_delete_pet_with_zero_id(self, pet_api):
        """Test deleting pet with zero ID"""
        pet_id = 0
        response = pet_api.delete_pet(pet_id)
        assert response.status_code in [200, 404]

    def test_delete_pet_with_negative_id(self, pet_api):
        """Test deleting pet with negative ID"""
        pet_id = -1
        response = pet_api.delete_pet(pet_id)
        assert response.status_code in [200, 404, 400]
