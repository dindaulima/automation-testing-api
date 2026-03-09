import requests
from config.settings import BASE_URL, TIMEOUT


class PetAPI:
    """API client for Pet endpoints in Petstore API"""

    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
        self.endpoint = "/pet"

    def add_pet(self, pet_data):
        """Add a new pet to the store"""
        url = f"{self.base_url}{self.endpoint}"
        return requests.post(url, json=pet_data, timeout=self.timeout)

    def update_pet(self, pet_data):
        """Update an existing pet"""
        url = f"{self.base_url}{self.endpoint}"
        return requests.put(url, json=pet_data, timeout=self.timeout)

    def get_pet_by_id(self, pet_id):
        """Get pet by ID"""
        url = f"{self.base_url}{self.endpoint}/{pet_id}"
        return requests.get(url, timeout=self.timeout)

    def update_pet_with_form(self, pet_id, name=None, status=None):
        """Update pet with form data"""
        url = f"{self.base_url}{self.endpoint}/{pet_id}"
        data = {}
        if name:
            data["name"] = name
        if status:
            data["status"] = status
        return requests.post(url, data=data, timeout=self.timeout)

    def delete_pet(self, pet_id):
        """Delete a pet"""
        url = f"{self.base_url}{self.endpoint}/{pet_id}"
        return requests.delete(url, timeout=self.timeout)

    def find_pets_by_status(self, status):
        """Find pets by status"""
        url = f"{self.base_url}{self.endpoint}/findByStatus"
        params = {"status": status} if isinstance(status, str) else {"status": status}
        return requests.get(url, params=params, timeout=self.timeout)

    def find_pets_by_tags(self, tags):
        """Find pets by tags"""
        url = f"{self.base_url}{self.endpoint}/findByTags"
        params = {"tags": tags} if isinstance(tags, list) else {"tags": [tags]}
        return requests.get(url, params=params, timeout=self.timeout)

    def upload_pet_image(self, pet_id, image_file, additional_metadata=None):
        """Upload an image for a pet"""
        url = f"{self.base_url}{self.endpoint}/{pet_id}/uploadImage"
        files = {"file": image_file}
        data = {}
        if additional_metadata:
            data["additionalMetadata"] = additional_metadata
        return requests.post(url, files=files, data=data, timeout=self.timeout)
