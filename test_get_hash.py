import pytest
import requests
import json
import base64

@pytest.fixture
def base_url():
    return "http://127.0.0.1:8088"

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False

def test_valid_get_hash(base_url):
    url = base_url + "/hash/1"
    headers = {'Accept':'application/json'}
    response = requests.get(url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert(isBase64(response.text))
