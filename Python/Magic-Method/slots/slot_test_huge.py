import random
import time
from typing import List, Tuple

from memory_profiler import profile


class Profit(object):

    def __init__(self, name: str, desc: str, something: str, value: int, price: int, tax: int):
        self.name = name
        self.desc = desc
        self.something = something
        self.value = value
        self.price = price
        self.tax = tax

    def clear(self):
        self.name = ''
        self.desc = ''
        self.something = ''
        self.value = 0
        self.price = 0
        self.tax = 0


class ProfitUsingSlot(object):
    __slots__ = ['name', 'value', 'desc', 'something', 'price', 'tax', ]

    def __init__(self, name: str, desc: str, something: str, value: int, price: int, tax: int):
        self.name = name
        self.desc = desc
        self.something = something
        self.value = value
        self.price = price
        self.tax = tax

    def clear(self):
        self.name = ''
        self.desc = ''
        self.something = ''
        self.value = 0
        self.price = 0
        self.tax = 0


COUNT: int = int(1e4)


@profile
def create_things() -> Tuple[List[Profit], List[ProfitUsingSlot]]:
    start_time = time.time()
    profits = [
        Profit(
            name = f"name-{i}",
            desc = f"name-{i}'s sample",
            something = "this is something property",
            value = random.randint(0, COUNT),
            price = random.randint(0, COUNT),
            tax = random.randint(0, COUNT),
        ) for i in range(COUNT)]
    print(f"Profit create time : {time.time() - start_time}")
    del start_time

    start_time = time.time()
    profitUsingSlots = [
        ProfitUsingSlot(
            name = f"name-{i}",
            desc = f"name-{i}'s sample",
            something = "this is something property",
            value = random.randint(0, COUNT),
            price = random.randint(0, COUNT),
            tax = random.randint(0, COUNT),
        ) for i in range(COUNT)]
    print(f"ProfitUsingSlot create time : {time.time() - start_time}")
    return profits, profitUsingSlots


def manipulate_things(profits: List[Profit], profitUsingSlots: List[ProfitUsingSlot]):
    start_time = time.time()
    for p in profits:
        p.clear()
    print(f"Profit manipulate time : {time.time() - start_time}")
    del start_time

    start_time = time.time()
    for p in profitUsingSlots:
        p.clear()
    print(f"ProfitUsingSlots manipulate time : {time.time() - start_time}")


profits, profitUsingSlots = create_things()
manipulate_things(profits, profitUsingSlots)
