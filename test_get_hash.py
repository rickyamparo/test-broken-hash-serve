import pytest
import requests
import json
import base64
import os
import time

@pytest.fixture
def base_url():
    return "http://127.0.0.1:" + str(os.environ['PORT'])

def create_hash_id(base_url):
    data = {'password':'angrymonkey'}
    headers = {'Accept':'application/json'}
    response = requests.post(base_url + "/hash", json=data, headers=headers)
    return response.text

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False

def test_valid_get_hash(base_url):
    hash_id = create_hash_id(base_url)
    url = base_url + "/hash/" + str(hash_id)
    headers = {'Accept':'application/json'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert(isBase64(response.text))