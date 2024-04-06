import requests


def test_put():
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url)

    assert response.status_code == 204


def test_delete_non_existent_user():
    url = "https://reqres.in/if_not_found_user"

    response = requests.delete(url)

    assert response.status_code == 404
