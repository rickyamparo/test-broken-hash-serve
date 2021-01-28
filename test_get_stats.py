import pytest
import requests
import json
import os

@pytest.fixture
def base_url():
    return "http://127.0.0.1:" + str(os.environ['PORT'])

def test_valid_get_stats(base_url):
    url = base_url + "/stats"
    response = requests.get(url)
    response_body = json.loads(response.text)
    assert response_body['TotalRequests']
    assert response_body['AverageTime']
    assert response.status_code == 200