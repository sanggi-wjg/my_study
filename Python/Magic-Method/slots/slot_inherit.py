# 이렇게 하면 에러 발생
# class Base_A(object):
#     __slots__ = ['a']
#
#
# class Base_B(object):
#     __slots__ = ['b']
#
#
# class Sample(Base_A, Base_B):
#     pass
#
#
# s = Sample()
# END
from abc import ABC


class Base_A(object):
    __slots__ = ('a',)

class Base_B(object):
    __slots__ = ('b',)

class Sample():
    __slots__ = ('a','b')

s = Sample()
