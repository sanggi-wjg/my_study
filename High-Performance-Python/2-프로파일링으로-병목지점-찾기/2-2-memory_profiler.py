from typing import Tuple

from memory_profiler import profile


@profile
def something_method() -> Tuple[int, int]:
    a = [1] * (10 ** 5)
    b = [2] * (2 * 10 ** 6)
    c = [3] * (3 * 10 ** 7)
    del c
    return a, b


results = something_method()
