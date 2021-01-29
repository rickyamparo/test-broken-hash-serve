import pytest
import requests
import json
import os
import asyncio

async def test_make_request():
    url = "http://127.0.0.1:" + str(os.environ['PORT']) + "/stats"
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