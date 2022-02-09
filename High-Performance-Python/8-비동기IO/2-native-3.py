import asyncio

import requests


async def request_ping():
    url = "http://localhost:9000/long_sync"
    res = requests.get(url)
    print(res.text)


async def request_hello():
    url = "http://localhost:9000/long_sync"
    res = requests.get(url)
    print(res.text)


async def something_method():
    task1 = asyncio.create_task(request_ping())
    task2 = asyncio.create_task(request_hello())
    await task1
    await task2


asyncio.run(something_method())
