# jkapis
JK APIs - Sample Package

## APIInterface

The `APIInterface` class allows you to interact with multiple APIs using a common interface.

### Initialization

```python
from jkapis import APIInterface

api = APIInterface(base_url="https://api.example.com", token="your_token_here")
```

### Methods

- `get(endpoint, params=None)`: Sends a GET request to the specified endpoint.
- `post(endpoint, data=None)`: Sends a POST request to the specified endpoint.

### Example Usage

```python
# Initialize the API interface
api = APIInterface(base_url="https://api.example.com", token="your_token_here")

# Make a GET request
response = api.get("some/endpoint")
print(response)

# Make a POST request
response = api.post("some/endpoint", data={"key": "value"})
print(response)
```