import math


@profile
def calculate_something(size = 1000):
    temp = [0] * size
    for i in range(size):
        temp[i] = math.factorial(i)
    return temp


t = calculate_something()
