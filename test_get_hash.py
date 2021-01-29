import pytest
import requests
import json
import base64
import time
from helper import Helper

test_helper = Helper()

def test_valid_get_hash():
    hash_id = test_helper.create_hash_id().text
    url = test_helper.base_url() + "/hash/" + str(hash_id)
    headers = {'Accept':'application/json'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert(test_helper.isBase64(response.text))