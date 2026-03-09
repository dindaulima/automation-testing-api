import pytest


@pytest.mark.pet
@pytest.mark.regression
class TestPetUpdate:
    """Test cases for pet update endpoints"""

    def test_update_pet_success(self, pet_api):
        """Test updating an existing pet"""
        pet_data = {
            "id": 1,
            "name": "UpdatedPet",
            "photoUrls": ["http://example.com/updated.jpg"],
            "status": "sold"
        }
        response = pet_api.update_pet(pet_data)
        assert response.status_code == 200

    def test_update_pet_status(self, pet_api):
        """Test updating only the pet status"""
        pet_data = {
            "id": 1,
            "name": "TestPet",
            "photoUrls": ["http://example.com/pet.jpg"],
            "status": "pending"
        }
        response = pet_api.update_pet(pet_data)
        assert response.status_code == 200

    def test_update_pet_with_form_data(self, pet_api):
        """Test updating pet with form data"""
        pet_id = 1
        response = pet_api.update_pet_with_form(pet_id, name="FormUpdatedPet", status="sold")
        assert response.status_code == 200

    def test_update_pet_name_only(self, pet_api):
        """Test updating only pet name"""
        pet_id = 1
        response = pet_api.update_pet_with_form(pet_id, name="NewName")
        assert response.status_code == 200

    def test_update_pet_status_only(self, pet_api):
        """Test updating only pet status"""
        pet_id = 1
        response = pet_api.update_pet_with_form(pet_id, status="available")
        assert response.status_code == 200

    def test_update_pet_with_special_characters(self, pet_api):
        """Test updating pet with special characters"""
        pet_data = {
            "id": 1,
            "name": "Spécial®™",
            "photoUrls": ["http://example.com/pet.jpg"],
            "status": "available"
        }
        response = pet_api.update_pet(pet_data)
        assert response.status_code == 200

    def test_update_nonexistent_pet(self, pet_api):
        """Test updating a non-existent pet"""
        pet_data = {
            "id": 99999999,
            "name": "NonExistent",
            "photoUrls": ["http://example.com/pet.jpg"],
            "status": "available"
        }
        response = pet_api.update_pet(pet_data)
        # May return 404 or 200 depending on API behavior
        assert response.status_code in [200, 404]

    def test_update_pet_with_multiple_tags(self, pet_api):
        """Test updating pet with multiple tags"""
        pet_data = {
            "id": 1,
            "name": "TaggedPet",
            "photoUrls": ["http://example.com/pet.jpg"],
            "status": "available",
            "tags": [
                {"id": 1, "name": "tag1"},
                {"id": 2, "name": "tag2"},
                {"id": 3, "name": "tag3"}
            ]
        }
        response = pet_api.update_pet(pet_data)
        assert response.status_code == 200
