import pytest
import requests
import json
import time
from helper import Helper

test_helper = Helper()

# Checks if we can successfully create a hash identifier after the app has proccessed for 5 minutes
def test_valid_post_hash():
    begin = time.time()
    response = test_helper.create_hash_id()
    end = time.time()
    hash_id = json.loads(response.text)
    assert response.status_code == 200
    assert round(end - begin) == 5
    assert isinstance(hash_id, int)