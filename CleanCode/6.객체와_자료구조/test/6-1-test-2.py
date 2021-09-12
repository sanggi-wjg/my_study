import math


class Point(object):
    x: float
    y: float


class Figure(object):
    point: Point

    def get_area(self) -> float:
        raise NotImplementedError("Not Implemented")


class Squre(Figure):
    side: float

    def get_area(self) -> float:
        return self.side * self.side


class Rectangle(Figure):
    width: float
    height: float

    def get_area(self) -> float:
        return self.width * self.height


class Circle(Figure):
    radius: float

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius
