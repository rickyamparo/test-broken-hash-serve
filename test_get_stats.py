import pytest
import requests
import json
import os
import time
from helper import Helper

test_helper = Helper()

test_helper.open_app()
time.sleep(1)

def test_valid_get_stats():
    url = test_helper.base_url() + "/stats"
    response = requests.get(url)
    response_body = json.loads(response.text)
    assert response_body['TotalRequests']
    assert response_body['AverageTime']
    assert response.status_code == 200

def test_no_body():
    url = test_helper.base_url() + "/stats"
    data = {'password':'angrymonkey'}
    response = requests.get(url, data=data)
    assert response == 400

def test_is_valid_json():
    url = test_helper.base_url() + "/stats"
    response = requests.get(url)
    assert test_helper.is_json(response.text)