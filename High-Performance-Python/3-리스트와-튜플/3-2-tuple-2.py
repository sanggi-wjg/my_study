import timeit

t1 = timeit.timeit('t = (1,2,3,4,5,6,7,8,9)', number = 10)
t2 = timeit.timeit('t = (1,2,3,4,5,6,7,8,9)', number = 10)
t3 = timeit.timeit('t = (1,2,3,4,5,6,7,8,9)', number = 10)

print('tuple', t1)
print('tuple', t2)
print('tuple', t3)
