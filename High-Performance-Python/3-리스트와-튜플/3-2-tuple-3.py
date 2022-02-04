import timeit

t1 = timeit.timeit("""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(11, 21):
    l.append(i)
for i in range(21, 31):
    l.append(i)
""", number = 10)

t2 = timeit.timeit("""
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tt = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
ttt = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
t = t + tt
t = t + ttt
""", number = 10)

print('List', t1)
print('Tuple', t2)
