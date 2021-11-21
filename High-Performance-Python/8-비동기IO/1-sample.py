import asyncio
import random
import string

import aiohttp as aiohttp


class AsyncBatcher(object):

    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.batch = []
        self.client_session = None
        self.url = "http://localhost:9000/ping"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()

    def save(self, result):
        self.batch.append(result)
        if len(self.batch) == self.batch_size:
            self.flush()

    def flush(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__aflush())

    async def __aflush(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(result, session) for result in self.batch]

            for task in asyncio.as_completed(tasks):
                await task
            self.batch.clear()

    async def fetch(self, result, session):
        async with session.post(self.url, data = result) as response:
            return await response.json()


def do_task(difficulty):
    return [i for i in range(difficulty * 100)]


with AsyncBatcher(100) as batcher:
    for i in range(100):
        batcher.save(do_task(i))
