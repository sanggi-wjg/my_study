class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 1)
p2 = Point(1, 1)
s = { p1, p2 }
print(type(s), s)
print(Point(1, 1) in s)