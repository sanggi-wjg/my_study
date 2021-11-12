import sys


# a = []
# print('0', sys.getsizeof(a))
#
# a.append(1)
# print('1', sys.getsizeof(a))
#
# a.append(2)
# print('2', sys.getsizeof(a))
#
# a.append(3)
# print('3', sys.getsizeof(a))
#
# a.append(4)
# print('4', sys.getsizeof(a))
#
# a.append(5)
# print('5', sys.getsizeof(a))

# a = []
# for i in range(1, 10000):
#     a.append(i)
#     print(i, sys.getsizeof(a))

def create_list_1():
    a = []
    for i in range(1, 100001):
        a.append(i)


def create_list_2():
    return [i for i in range(1, 100001)]


create_list_1()
create_list_2()
