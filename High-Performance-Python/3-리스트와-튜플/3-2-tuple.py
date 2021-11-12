import sys

l = [i for i in range(100000)]
t = tuple(l)

print('list', sys.getsizeof(l))
print('tuple', sys.getsizeof(t))
