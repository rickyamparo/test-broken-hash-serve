import pytest
import requests
import time
from helper import Helper

test_helper = Helper()

# Checks if the application can be properly intialized and listening for HTTP requests
def test_proper_intialize():
    test_helper.open_app()
    time.sleep(1)
    url = test_helper.base_url() + '/stats'
    try:
        requests.get(url)
        assert True
    except requests.ConnectionError:
        assert False

# Checks to see if the application can succesfully shutdown via request
def test_graceful_shutdown():
    time.sleep(1)
    url = test_helper.base_url() + '/hash'
    data = 'shutdown'
    response = requests.post(url, data=data)
    assert response.status_code == 200

# Checks to see if the application will not accept requests after shutting down
def test_no_additional_requests():
    url = test_helper.base_url() + "/hash"
    data = {'password':'angrymonkey'}
    headers = {'Accept':'application/json'}
    try:
        requests.post(url, data=data, headers=headers)
        assert False
    except requests.ConnectionError:
        assert True
