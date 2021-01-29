import pytest
import requests
import subprocess
import os
import time

@pytest.fixture 
def open_app():
    return subprocess.Popen(['open','/Users/rickyamparo/broken-hashserve/broken-hashserve_darwin'])

@pytest.fixture
def base_url():
    return "http://127.0.0.1:" + str(os.environ['PORT'])

def test_graceful_shutdown(base_url,open_app):
    open_app
    time.sleep(2)
    url = base_url + '/hash'
    data = 'shutdown'
    response = requests.post(url, data=data)
    assert response.status_code == 200

def test_no_additional_requests(base_url):
    url = base_url + "/hash"
    data = {'password':'angrymonkey'}
    headers = {'Accept':'application/json'}
    try:
        requests.post(url, data=data, headers=headers)
        assert False
    except requests.ConnectionError:
        assert True
