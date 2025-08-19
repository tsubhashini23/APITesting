import requests
import json

url='https://reqres.in/api/users'

head = {
    'Content-Type': 'application/json',
    'x-api-key': 'reqres-free-v1'
}

#
# payload = {
#   "name": "anjana",
#   "job": "QA"
# }

json_file = open('./users.json')
json_payload = json.load(json_file)

response = requests.post(url,headers = head,json = json_payload)

# response = requests.post(url,headers = head,data = json.dumps(json_payload))

print(response.json())
# print(response.text)
assert response.status_code == 201

# getResponse = requests.get(url+"/"+str(response.json()["id"]), headers = head)
#
# print(getResponse.json())

