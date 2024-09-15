import requests

# Define the endpoint URL
url = "http://127.0.0.1:8000/sales/stores/items/"

# Define the query parameters
params = {
    "date": "2024-09-15",
    "store_id": 1,
    "item_id": 42
}

# Send the GET request with query parameters
response = requests.get(url, params=params)

# Print the response status code and JSON content
print("Status Code:", response.status_code)
print("Response JSON:", response.json())