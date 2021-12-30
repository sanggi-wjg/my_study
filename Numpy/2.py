import sys
import time

import numpy as np

size = 1000000

start_time = time.time()
list1 = [i for i in range(size)]
list2 = [i for i in range(size)]
result_list = [a * b for a, b in zip(list1, list2)]
print(time.time() - start_time, sys.getsizeof(result_list))
del start_time

start_time = time.time()
array1 = np.arange(size)
array2 = np.arange(size)
result_array = array1 * array2
print(time.time() - start_time, sys.getsizeof(result_array))
