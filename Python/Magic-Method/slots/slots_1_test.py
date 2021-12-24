import sys


class Normal(object):

    def __init__(self, foo, some, any):
        self.foo = foo
        self.some = some
        self.any = any


class UsingSlots(object):
    __slots__ = ['foo', 'some', 'any']

    def __init__(self, foo, some, any):
        self.foo = foo
        self.some = some
        self.any = any


use_slots = UsingSlots('var', 'thing', 'thing2')
use_slots.a = 'a'

# output
# 48 {'foo': 'var', 'some': 'thing', 'any': 'thing'} 104
# 56 ['foo', 'some', 'any'] 80
