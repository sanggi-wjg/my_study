import asyncio
from urllib.request import Request, urlopen


async def fetch(num):
    request = Request('http://localhost:9000/ping')
    response = await loop.run_in_executor(None, urlopen, request)
    return num, response


async def ping():
    tasks = [asyncio.ensure_future(
        fetch(i)
    ) for i in range(100)]

    result = await asyncio.gather(*tasks)
    print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(ping())
loop.close()
