import csv
from typing import List, Tuple


def read_csv() -> Tuple[list, list]:
    before, after = [], []
    file = open('change_test.csv', 'r')
    try:
        for row in csv.reader(file):
            before.append(row[0])
            after.append(row[1])
    finally:
        file.close()
    return before, after


def check(after_stc: str) -> str:
    if after_stc not in BEFORE_STCS:
        return after_stc
    else:
        index = BEFORE_STCS.index(after_stc)
        BEFORE_STCS.pop(index)
        return check(
            AFTER_STCS.pop(index)
        )


BEFORE_STCS, AFTER_STCS = read_csv()

"""
    A 

    A -> B

    A -> B
    B -> C

    A -> B
    B -> C
    C -> D

    ...

    이런 상황
    """

results = []
while AFTER_STCS:
    _, after_stc = BEFORE_STCS.pop(0), AFTER_STCS.pop(0)
    results.append(
        check(after_stc)
    )
