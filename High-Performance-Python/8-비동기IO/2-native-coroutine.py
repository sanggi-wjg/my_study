import asyncio

from openpyxl import load_workbook


async def load(path):
    workbook = load_workbook(path, read_only = True, data_only = True)
    return workbook


async def something_big():
    return [i for i in range(10000000)]


async def something_small():
    return [i for i in range(1000000)]


async def get_sheet_and_somethings(path):
    task1 = asyncio.create_task(load(path))
    task2 = asyncio.create_task(something_big())
    task3 = asyncio.create_task(something_small())
    await task1
    await task2
    await task3
    return task1.result()

result = asyncio.run(get_sheet_and_somethings('YTO-2021-10-SHA.xlsx'))

