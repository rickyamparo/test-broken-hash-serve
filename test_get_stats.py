import pytest
import requests
import json
import os
import time
from helper import Helper

test_helper = Helper()

test_helper.open_app()
time.sleep(1)
test_helper.create_hash_id()

# Checks if we're able to retrieve valid stats in JSON format
def test_valid_get_stats():
    url = test_helper.base_url() + "/stats"
    response = requests.get(url)
    response_body = json.loads(response.text)
    assert response_body['TotalRequests']
    assert response_body['AverageTime']
    assert response.status_code == 200

# Checks to see that no data can be passed along the body in the GET request
def test_no_body():
    url = test_helper.base_url() + "/stats"
    data = {'password':'angrymonkey'}
    response = requests.get(url, data=data)
    assert response == 400

# Checks to make sure that the JSON returned is valid
def test_is_valid_json():
    url = test_helper.base_url() + "/stats"
    response = requests.get(url)
    assert test_helper.is_json(response.text)