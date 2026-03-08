import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://petstore.swagger.io/v2")
API_KEY = os.getenv("API_KEY", "special-key")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))
