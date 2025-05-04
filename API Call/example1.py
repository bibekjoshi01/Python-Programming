import requests

# Define the API endpoint
BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/1")

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
