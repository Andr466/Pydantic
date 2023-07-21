from models import AccessTokenRequest
import pytest


def test_access_token_required():
    request = {
        "access_token": "token123"
    }
    AccessTokenRequest(**request)


def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)