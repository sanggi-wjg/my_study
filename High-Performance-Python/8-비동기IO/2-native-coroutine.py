import asyncio

import aiohttp


async def request_long_sync():
    url = "http://localhost:9000/long_sync"
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as res:
            print(await res.read())


async def async_method():
    task1 = asyncio.create_task(request_long_sync())
    task2 = asyncio.create_task(request_long_sync())
    await task1
    await task2


asyncio.run(async_method())
