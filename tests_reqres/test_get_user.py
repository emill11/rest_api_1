import requests
from jsonschema import validate
from schemas.get_list_users import GetUsers


def test_get():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url=url)

    assert response.json()['total_pages'] == 2
    assert response.status_code == 200


def test_get_not_found():
    url = "https://reqres.in/_not_found"
    response = requests.get(url=url)

    assert response.status_code == 404


def test_get_schema_validation():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url=url)

    validate(response.json(), GetUsers)
