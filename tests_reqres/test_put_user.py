import requests
from jsonschema import validate

from schemas.put_update_user import PutUbdate


def test_put():
    url = "https://reqres.in/api/users/2"

    name = 'asdf'
    job = 'qwerty'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.put(url, payload)

    assert response.json()['name'] == 'asdf'
    assert response.status_code == 200


def test_put_no_body():
    url = "https://reqres.in/api/users/2"
    payload = {}
    response = requests.put(url, payload)

    assert response.status_code == 200


def test_put_non_existent_user():
    url = "https://reqres.in/if_not_found_user"
    name = 'asdf'
    job = 'qwerty'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.put(url, payload)

    assert response.status_code == 404


def test_put_schema_validation():
    url = "https://reqres.in/api/users/2"
    name = 'aaaa'
    job = 'bbbb'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.put(url, payload)

    validate(response.json(), PutUbdate)
