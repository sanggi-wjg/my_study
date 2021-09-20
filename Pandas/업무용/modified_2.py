import csv
from typing import Tuple


def read_csv(filename: str) -> Tuple[list, list]:
    before, after = [], []
    file = open(filename, 'r')
    try:
        for row in csv.reader(file):
            before.append(row[0])
            after.append(row[1])
    finally:
        file.close()
    return before, after


def write_csv(filename: str, datalist: list):
    file = open(filename, 'w', newline = '')
    try:
        writer = csv.writer(file)
        for data in datalist:
            writer.writerow([data])
    finally:
        file.close()


def check(after_stc: str) -> str:
    if after_stc not in BEFORE_STCS:
        return after_stc
    else:
        index = BEFORE_STCS.index(after_stc)
        BEFORE_STCS.pop(index)
        return check(
            AFTER_STCS.pop(index)
        )


"""
A -> B

A -> B
B -> C

A -> B
B -> C
C -> D
...
"""
READ_FILENAME, WRITE_FILENAME = 'change.csv', 'result.csv'
BEFORE_STCS, AFTER_STCS = read_csv(READ_FILENAME)

results = []
while AFTER_STCS:
    _, after_stc = BEFORE_STCS.pop(0), AFTER_STCS.pop(0)
    results.append(
        check(after_stc)
    )

write_csv(WRITE_FILENAME, results)
