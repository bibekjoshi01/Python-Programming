import requests

response = requests.post("https://httpbin.org/post", data={"key": "value"})
print(response.json())
