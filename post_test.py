import pytest
import requests
import json

@pytest.fixture
def base_url():
    return "http://127.0.0.1:8088"

def test_valid_post_hash(base_url):
    url = base_url + "/hash"
    data = {'password':'angrymonkey'}
    headers = {'Accept':'application/json'}
    response = requests.post(url, json=data, headers=headers)
    hash_id = json.loads(response.text)
    assert response.status_code == 200
    assert isinstance(hash_id, str)