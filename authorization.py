import requests
import time

#Authorization

head = {
    "Content-Type": "application/json",
    "Authorization": "Bearer acd38cd5959b600a1761215776093197151d5f39a468d752a8c4eb21a10e5b46"
}

data = {
  "name": "decor",
  "email": f"queen_{int(time.time())}@gmail.com",
  "gender": "female",
  "status": "active"
}

url = "https://gorest.co.in/public/v2/users"

#POST with authorization

postResponse = requests.post(url, headers = head, json = data)

print(postResponse.status_code)
print(postResponse.json())

assert postResponse.json()["name"] == "decor"

#GET with authorization

getResponse = requests.get(url+"/"+str(postResponse.json()["id"]), headers = head)

print(getResponse.json())

assert getResponse.json()["name"] == "decor"