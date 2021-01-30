import pytest
import requests
import asyncio
from helper import Helper

test_helper = Helper()

# Tests to see if multple simulateneous requests can be handled by the application
async def test_make_request():
    url = test_helper.base_url() + "/stats"
    response = requests.get(url)
    assert response.status_code == 200
    await asyncio.sleep(0.1)

async def main():
    await asyncio.wait([
        test_make_request(),
        test_make_request()
    ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())