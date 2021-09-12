import copy


class Point(object):

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
        self._is_marked = False

    def mark_dot(self):
        self._is_marked = True

    @property
    def is_marked(self):
        return self._is_marked

    def unmark_dot(self):
        self._is_marked = False

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x: float):
        self._x = x

    @y.setter
    def y(self, y: float):
        self._y = y

    def show(self):
        print('X:', self.x, ' / Y:', self.y, ' / Marking:', self.is_marked)


"""
X: 10.0  / Y: 10.0  / Marking: True
X: 20.0  / Y: 20.0  / Marking: False
2294031974536 
2294034256456
"""

point1 = Point(10.0, 10.0)
point1.mark_dot()

point2 = copy.deepcopy(point1)
point2.x = 20.0
point2.y = 20.0
point2.unmark_dot()

point1.show()
point2.show()
print(id(point1))
print(id(point2))
