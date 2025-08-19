import requests
import pytest

def test_validate_getrequests():
    head = {
        "Content-Type": "application/json",
        'Accept': 'text/plain'
    }
    url = 'https://reqres.in'

    getResponse = requests.get(url + '/api/users/2', headers=head)

    print(getResponse.json())
    print(getResponse.text)

    print(type(getResponse.json()))  # <class 'dict'>
    print(type(getResponse.text))  # <class 'str'>


    assert getResponse.status_code == 200