# Petstore API Testing Project

Automated API testing project for the Petstore Swagger API (https://petstore.swagger.io), with a focus on user endpoint testing.

## Project Structure

```
├── api/                      # API client implementations
│   ├── __init__.py
│   └── user_api.py          # User API endpoints client
├── config/                   # Configuration files
│   └── settings.py          # Environment and settings configuration
├── tests/                    # Test cases
│   ├── conftest.py          # Pytest fixtures and configuration
│   ├── test_user_create.py  # User creation tests
│   ├── test_user_read.py    # User retrieval tests
│   ├── test_user_update.py  # User update tests
│   ├── test_user_delete.py  # User deletion tests
│   └── test_user_auth.py    # User authentication tests
├── .env                      # Environment variables
├── .env.example             # Example environment variables
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Features

- **User API Testing**: Comprehensive test coverage for all user endpoints
  - Create users (single and batch)
  - Retrieve users
  - Update user information
  - Delete users
  - User authentication (login/logout)

- **Test Organization**: Tests organized by functionality with pytest markers
  - `@pytest.mark.user` - User-related tests
  - `@pytest.mark.smoke` - Quick smoke tests
  - `@pytest.mark.regression` - Regression tests

- **Fixtures**: Reusable fixtures for API client and test data
- **Configuration**: Environment-based configuration for flexible deployment

## Installation

1. **Clone the repository**
   ```bash
   cd /home/sevima-330/Documents/automation-testing-api
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit the `.env` file to configure the API settings:

```
BASE_URL=https://petstore.swagger.io/v2
API_KEY=special-key
TIMEOUT=10
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run only user tests
```bash
pytest -m user
```

### Run smoke tests
```bash
pytest -m smoke
```

### Run with verbose output
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_user_create.py
```

### Run with coverage report
```bash
pytest --cov=api --cov=config
```

### Run with allure report
```bash
pytest --allure-dir=allure-results
allure serve allure-results
```

## Test Cases

### User Creation Tests (`test_user_create.py`)
- Create a single user
- Create user with minimal data
- Create multiple users
- Create user with special characters
- Create user with long strings

### User Retrieval Tests (`test_user_read.py`)
- Get user by username
- Get user with special characters
- Get non-existent user
- Validate response structure
- Get user with numeric username
- Get user with empty username

### User Update Tests (`test_user_update.py`)
- Update existing user
- Partial user update
- Update non-existent user
- Update specific fields
- Update with special characters
- Update with empty body

### User Deletion Tests (`test_user_delete.py`)
- Delete existing user
- Delete non-existent user
- Delete user with special characters
- Delete user with numeric username
- Validate deletion response
- Delete with empty username

### User Authentication Tests (`test_user_auth.py`)
- Successful login
- Login with invalid credentials
- Login with empty username/password
- Login with special characters
- Validate login response structure
- User logout

## Dependencies

- **requests** - HTTP client library
- **pytest** - Testing framework
- **pytest-cov** - Code coverage plugin
- **python-dotenv** - Environment variable management
- **allure-pytest** - Test reporting

## Best Practices Implemented

1. **DRY Principle** - API client abstraction to avoid code duplication
2. **Fixtures** - Reusable test data and client setup
3. **Markers** - Organized test execution with pytest markers
4. **Configuration** - Environment-based configuration
5. **Error Handling** - Tests handle multiple response codes
6. **Documentation** - Clear test names and docstrings

## Future Enhancements

- [ ] Add more API endpoints (Pet, Store)
- [ ] Implement response validation schemas
- [ ] Add performance testing
- [ ] Add authentication token handling
- [ ] Add request/response logging
- [ ] Add database validation
- [ ] Add API contract testing

## Troubleshooting

### Tests timeout
Increase `TIMEOUT` in `.env` file

### Import errors
Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Connection errors
Verify `BASE_URL` in `.env` is accessible

## Author

API Testing Project

## License

MIT
