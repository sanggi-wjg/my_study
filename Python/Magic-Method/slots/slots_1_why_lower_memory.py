import sys


class Normal(object):
    pass


class UsingSlots(object):
    __slots__ = ['foo', 'some', 'any']


normal = Normal()
use_slots = UsingSlots()


def show_sizeof(cls):
    setattr(cls, 'foo', 'var')
    setattr(cls, 'some', 'thing')
    setattr(cls, 'any', 'thing')
    if hasattr(cls, '__dict__'):
        print(cls.__dict__, sys.getsizeof(cls.__dict__))
    else:
        print(cls.__slots__, sys.getsizeof(cls.__slots__))


show_sizeof(normal)
show_sizeof(use_slots)

# output
# 48 {'foo': 'var', 'some': 'thing', 'any': 'thing'} 104
# 56 ['foo', 'some', 'any'] 80
