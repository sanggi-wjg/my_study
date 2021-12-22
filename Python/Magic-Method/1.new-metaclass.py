class MyPointMeta(type):

    def __new__(mcs, name, bases, namespace):
        namespace['desc'] = 'My Point Meta Class'
        namespace['show'] = lambda self: print(self.x, self.y)
        return super().__new__(mcs, name, bases, namespace)


class MyPoint(metaclass = MyPointMeta):

    def __init__(self, x, y):
        self.x = x
        self.y = y


point = MyPoint(1, 2)
print(point.desc)
point.show()
