import timeit


def factorial_go():
    import ctypes

    library = ctypes.cdll.LoadLibrary('./go_library.so')
    library.Factorial.argtypes = [ctypes.c_longlong]

    for i in range(10, 20):
        library.Factorial(i)


def factorial_python():
    import math
    for i in range(10, 20):
        print(math.factorial(i))


def total_add_go():
    import ctypes

    library = ctypes.cdll.LoadLibrary('./go_library.so')
    library.TotalAdd.argtypes = [ctypes.c_int, ctypes.c_int]

    library.TotalAdd(1, 10000)


def total_add_python():
    return sum([i for i in range(1, 10000)])


"""
factorial

%timeit -n 10 factorial_go()
84.1 µs ± 25 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit -n 10 factorial_python()
40.6 µs ± 12.2 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)


total_add

%timeit -n 10 total_add_go()
82.5 µs ± 148 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit -n 10 total_add_python()
274 µs ± 16.3 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
"""
