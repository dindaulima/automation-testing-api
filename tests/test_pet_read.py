import pytest


@pytest.mark.pet
@pytest.mark.regression
class TestPetRead:
    """Test cases for pet retrieval endpoints"""

    def test_get_pet_by_id_success(self, pet_api):
        """Test retrieving a pet by ID"""
        pet_id = 100
        response = pet_api.get_pet_by_id(pet_id)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == pet_id

    def test_get_pet_response_structure(self, pet_api):
        """Test response structure for pet retrieval"""
        pet_id = 1
        response = pet_api.get_pet_by_id(pet_id)
        if response.status_code == 200:
            data = response.json()
            assert "id" in data
            assert "name" in data
            assert "photoUrls" in data

    def test_get_nonexistent_pet(self, pet_api):
        """Test retrieving a non-existent pet"""
        pet_id = 99999999
        response = pet_api.get_pet_by_id(pet_id)
        assert response.status_code == 404

    def test_find_pets_by_status_available(self, pet_api):
        """Test finding pets with available status"""
        response = pet_api.find_pets_by_status("available")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_find_pets_by_status_pending(self, pet_api):
        """Test finding pets with pending status"""
        response = pet_api.find_pets_by_status("pending")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_find_pets_by_status_sold(self, pet_api):
        """Test finding pets with sold status"""
        response = pet_api.find_pets_by_status("sold")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_find_pets_by_multiple_statuses(self, pet_api):
        """Test finding pets by multiple statuses"""
        statuses = ["available", "pending"]
        for status in statuses:
            response = pet_api.find_pets_by_status(status)
            assert response.status_code == 200

    def test_get_pet_with_invalid_id(self, pet_api):
        """Test retrieving pet with invalid ID format"""
        pet_id = "invalid"
        response = pet_api.get_pet_by_id(pet_id)
        # Should return 404 or 400
        assert response.status_code in [400, 404]

    def test_find_pets_by_tags(self, pet_api):
        """Test finding pets by tags"""
        response = pet_api.find_pets_by_tags(["friendly"])
        # May return 200 or 400 depending on API state
        assert response.status_code in [200, 400]
