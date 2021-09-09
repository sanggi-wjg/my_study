from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def do_something(self, data: list) -> list:
        pass


class StrategyA(Strategy):

    def do_something(self, data: list) -> list:
        return sorted(data)


class StrategyB(Strategy):

    def do_something(self, data: list) -> list:
        return list(reversed(sorted(data)))


class Context:

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def operate(self, data: list):
        return self.strategy.do_something(data)


def client_code():
    strategy_a = StrategyA()
    strategy_b = StrategyB()
    data = ['b', 'a', 'c', 'e', 'd']

    context = Context(strategy_a)
    result = context.operate(data)
    print(result)

    context.strategy = strategy_b
    result = context.operate(data)
    print(result)


"""
['a', 'b', 'c', 'd', 'e']
['e', 'd', 'c', 'b', 'a']
"""
client_code()
