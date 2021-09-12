from typing import Dict


class Target:

    def __init__(self, content: str):
        self._content = content

    @property
    def content(self):
        return self._content


class Flyweight:

    def __init__(self):
        self._pools: Dict[str, Target] = dict()

    def get(self, content: str):
        pool = self._pools.get(content, None)
        if not pool:
            pool = Target(content)
            self._pools[content] = pool

        return pool


def client_code():
    flyweight = Flyweight()
    a = flyweight.get('TEST_A')
    print(a, a.content)
    b = flyweight.get('TEST_B')
    print(b, b.content)
    c = flyweight.get('TEST_C')
    print(c, c.content)
    a = flyweight.get('TEST_A')
    print(a, a.content)


"""
<__main__.Target object at 0x0000022F0BB55948> TEST_A
<__main__.Target object at 0x0000022F1C2C5E08> TEST_B
<__main__.Target object at 0x0000022F1D666988> TEST_C
<__main__.Target object at 0x0000022F0BB55948> TEST_A
"""

client_code()
