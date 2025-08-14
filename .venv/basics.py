import requests

#GET

header = {
    "Accept": "text/plain"
}

response = requests.get("https://fakerestapi.azurewebsites.net//api/v1/Activities/1")

print(response.status_code)
print(response.json())
#print(response)

assert response.status_code == 200