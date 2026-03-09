import pytest


@pytest.mark.pet
@pytest.mark.smoke
class TestPetCreate:
    """Test cases for pet creation endpoints"""

    def test_add_pet_success(self, pet_api, sample_pet):
        """Test adding a pet successfully"""
        response = pet_api.add_pet(sample_pet)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == sample_pet["name"]
        assert data["status"] == sample_pet["status"]

    def test_add_pet_with_minimal_data(self, pet_api):
        """Test adding a pet with minimal required data"""
        minimal_pet = {
            "id": 100,
            "name": "MinimalPet",
            "photoUrls": []
        }
        response = pet_api.add_pet(minimal_pet)
        assert response.status_code == 200

    def test_add_pet_with_special_characters(self, pet_api):
        """Test adding a pet with special characters"""
        pet = {
            "id": 101,
            "name": "Fluffy®™",
            "photoUrls": ["http://example.com/pet.jpg"],
            "status": "available"
        }
        response = pet_api.add_pet(pet)
        assert response.status_code == 200

    def test_add_pet_with_multiple_photos(self, pet_api):
        """Test adding a pet with multiple photo URLs"""
        pet = {
            "id": 102,
            "name": "PhotoPet",
            "photoUrls": [
                "http://example.com/photo1.jpg",
                "http://example.com/photo2.jpg",
                "http://example.com/photo3.jpg"
            ],
            "status": "available"
        }
        response = pet_api.add_pet(pet)
        assert response.status_code == 200

    def test_add_pet_with_tags(self, pet_api):
        """Test adding a pet with tags"""
        pet = {
            "id": 103,
            "name": "TaggedPet",
            "photoUrls": ["http://example.com/pet.jpg"],
            "status": "available",
            "tags": [
                {"id": 1, "name": "cute"},
                {"id": 2, "name": "friendly"}
            ]
        }
        response = pet_api.add_pet(pet)
        assert response.status_code == 200

    def test_add_pet_with_category(self, pet_api):
        """Test adding a pet with category"""
        pet = {
            "id": 104,
            "name": "CategorizedPet",
            "photoUrls": ["http://example.com/pet.jpg"],
            "status": "available",
            "category": {
                "id": 5,
                "name": "Birds"
            }
        }
        response = pet_api.add_pet(pet)
        assert response.status_code == 200
