import math


class Squre(object):
    x: float
    y: float
    side: float


class Rectangle(object):
    x: float
    y: float
    width: float
    height: float


class Circle(object):
    x: float
    y: float
    radius: float


def get_arae(figure: object) -> float:
    if isinstance(figure, Squre):
        return figure.side * figure.side

    elif isinstance(figure, Rectangle):
        return figure.width * figure.height

    elif isinstance(figure, Circle):
        return math.pi * figure.radius * figure.radius

    else:
        raise Exception('no such figure')
