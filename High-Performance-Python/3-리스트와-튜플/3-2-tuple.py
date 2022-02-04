import sys
import timeit

l = [i for i in range(100000)]
t = tuple(l)

print('list', sys.getsizeof(l))
print('tuple', sys.getsizeof(t))

t1 = timeit.timeit('list(i for i in range(100000))', number = 10)
t2 = timeit.timeit('tuple([i for i in range(100000)])', number = 10)

print('list', t1)
print('tuple', t2)
