import sys
import time

import numpy as np

s = 1000

start = time.time()
b = [[j for j in range(s)] for _ in range(s)]
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = b[i][j] + b[i][j]
print(time.time() - start, sys.getsizeof(b))

start = time.time()
a = np.array([[j for j in range(s)] for i in range(s)])
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = a[i][j] + a[i][j]
print(time.time() - start, sys.getsizeof(a))
del start


