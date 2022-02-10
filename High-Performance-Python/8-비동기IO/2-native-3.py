import asyncio

import aiohttp


async def request_long_sync():
    url = "http://localhost:9000/long_sync"
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as res:
            print(await res.read())


async def async_method():
    await asyncio.wait([
        request_long_sync(),
        request_long_sync()
    ])


asyncio.run(async_method())
