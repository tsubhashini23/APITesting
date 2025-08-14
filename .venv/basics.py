import requests

url_one = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

#GET Method(ALL)

head_one = {
    "Accept": "text/plain"
}

getResponse = requests.get(url_one , headers=head_one)

print(getResponse.status_code)
print(getResponse.json())

assert getResponse.status_code == 200

#GET Method(1 record)

url_two = "https://fakerestapi.azurewebsites.net/api/v1/Activities/2"

head_two = {
    "Accept": "text/plain"
}

getResponse = requests.get(url_two, headers=head_two)

print(getResponse.status_code)
print(getResponse.json())

assert getResponse.status_code == 200

#Post Method

url_post = "https://fakerestapi.azurewebsites.net/api/v1/Books"

head_post = {
    "Accept": "text/plain",
    "Content-Type": "application/json"
}

data = {

  "id": 300,
  "title": "TS",
  "description": "string",
  "pageCount": 100,
  "excerpt": "string",
  "publishDate": "2025-08-14T11:36:06.928Z"

}

postResponse = requests.post(url_post, headers = head_post, json = data)

print(postResponse.status_code)
print(postResponse.json())

assert postResponse.json()["title"] == "TS"

#PUT Method

url_put = "https://fakerestapi.azurewebsites.net/api/v1/Books/300"

head_put = {
    "Accept": "text/plain"
}

data = {

  "id": 300,
  "title": "Alchemist",
  "description": "string",
  "pageCount": 200,
  "excerpt": "string",
  "publishDate": "2025-08-14T11:36:06.928Z"

}

putResponse = requests.put(url_put, headers = head_put, json = data)

print(putResponse.status_code)
print(putResponse.json())

assert putResponse.json()["title"] == "Alchemist"

