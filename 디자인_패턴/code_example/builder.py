from abc import ABC, abstractmethod
from typing import Any


class Product1(object):

    def __init__(self):
        self._parts = []

    def add(self, part: Any) -> None:
        self._parts.append(part)

    def show_parts(self) -> None:
        print('\t'.join(self._parts))


class Builder(ABC):

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):

    def __init__(self):
        self._product = Product1()

    @property
    def product(self) -> Product1:
        return self._product

    def produce_part_a(self) -> None:
        self._product.add('Part A')

    def produce_part_b(self) -> None:
        self._product.add('Part B')

    def produce_part_c(self) -> None:
        self._product.add('Part C')


class Director(object):

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_minimal(self):
        self.builder.produce_part_a()

    def build_maximal(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


def client_code():
    director = Director()
    builder = ConcreteBuilder1()

    director.builder = builder
    director.build_minimal()
    builder.product.show_parts()

    director.build_maximal()
    builder.product.show_parts()

    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.show_parts()


client_code()
