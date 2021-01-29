import pytest
import requests
import json
import os

@pytest.fixture
def base_url():
    return "http://127.0.0.1:" + str(os.environ['PORT'])

def is_json(jsonobject):
    try:
        json.loads(jsonobject)
    except ValueError:
        return False
    return True

def test_valid_get_stats(base_url):
    url = base_url + "/stats"
    response = requests.get(url)
    response_body = json.loads(response.text)
    assert response_body['TotalRequests']
    assert response_body['AverageTime']
    assert response.status_code == 200

def test_no_body(base_url):
    url = base_url + "/stats"
    data = {'password':'angrymonkey'}
    response = requests.get(url, data=data)
    assert response == 400

def test_is_valid_json(base_url):
    url = base_url + "/stats"
    response = requests.get(url)
    assert is_json(response.text)