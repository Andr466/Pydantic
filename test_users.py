from models import User
import pytest


def test_users_get_response():
    response = [
        {"id": 111, "first_name": "Ivan", "last_name": "Ivanov"},
        {"id": 222, "first_name": "Petr", "last_name": "Petrov"}
    ]
    users = [User(**user) for user in response]


def test_users_get_success():
    response = [
        {"id": 111, "first_name": "Ivan", "last_name": "Ivanov"},
        {"id": 222, "first_name": "Petr", "last_name": "Petrov"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 2
    assert users[0].id == 111
    assert users[0].first_name == "Ivan"
    assert users[0].last_name == "Ivanov"


def test_users_get_no_users():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0


def test_user_format():
    user = {
        "id": "invalid_id_format",
        "first_name": "Ivan",
        "last_name": "Ivanov"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_name_format():
    user = {
        "id": 111,
        "first_name": "Ivan123",
        "last_name": "Ivanov"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_lastname_format():
    user = {
        "id": 111,
        "first_name": "Ivan",
        "last_name": "Ivanov123"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_users_get_one_user():
    response = [{"id": 111, "first_name": "Ivan", "last_name": "Ivanov"}]
    users = [User(**user) for user in response]
    assert len(users) == 1
    assert users[0].id == 111
    assert users[0].first_name == "Ivan"
    assert users[0].last_name == "Ivanov"


def test_users_get_invalid_response():
    response = [{"invalid_attr": "value"}]
    with pytest.raises(ValueError):
        users = [User(**user) for user in response]
