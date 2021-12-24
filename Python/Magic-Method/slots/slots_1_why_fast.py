import timeit


class Normal(object):
    pass


class UsingSlots(object):
    __slots__ = ['name']


normal = Normal()
use_slots = UsingSlots()


def fn_set_get_delete(cls):
    def set_get_delete():
        setattr(cls, 'name', 'foo var')
        getattr(cls, 'name')
        delattr(cls, 'name')

    return set_get_delete


r1 = timeit.repeat(fn_set_get_delete(normal))
r2 = timeit.repeat(fn_set_get_delete(use_slots))
print(r1)
print(r2)
# output
# [0.187666, 0.1858013, 0.17950610000000006, 0.1788223, 0.18067900000000003]
# [0.15390950000000014, 0.15378409999999998, 0.1545802999999999, 0.1493369, 0.1511072]
