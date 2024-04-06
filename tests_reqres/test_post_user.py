import requests
from jsonschema import validate

from schemas.post_create_user import PostCreate


def test_post():
    url = "https://reqres.in/api/users"
    name = 'asdf'
    job = 'qwerty'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.post(url, payload)

    assert response.json()['name'] == name
    assert response.status_code == 201


def test_post_no_body():
    url = "https://reqres.in/api/users"
    payload = {}
    response = requests.post(url, payload)

    assert response.status_code == 201


def test_post_non_existent_resource():
    url = "https://reqres.in/if_not_found_"
    name = 'asdf'
    job = 'qwerty'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.post(url, payload)

    assert response.status_code == 404


def test_post_register_missing_password():
    url = "https://reqres.in/api/register"
    email = "sydney@fife.com"

    payload = {
        "email": email
    }
    response = requests.post(url, payload)

    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"


def test_post_schema_validation():
    url = "https://reqres.in/api/users"
    name = 'asdf'
    job = 'qwerty'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.post(url, payload)

    validate(response.json(), PostCreate)
