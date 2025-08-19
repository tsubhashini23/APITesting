import requests

param = {
    'page': 3,
    'per_page': 1
}

url = 'https://gorest.co.in/public/v2/users'

head = {
    "Content-Type": "application/json",
    'Accept': 'text/plain'
}

response = requests.get(url, headers = head, params = param)

print(response.json())

assert response.status_code == 200