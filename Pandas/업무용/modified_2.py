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
        return check(AFTER_STCS.pop(index))


def check_2(before_stc: str, after_stc: str, result: str) -> str:
    result += f" {before_stc} -> {after_stc}"
    if after_stc not in BEFORE_STCS:
        return result
    else:
        index = BEFORE_STCS.index(after_stc)
        return check_2(BEFORE_STCS.pop(index), AFTER_STCS.pop(index), result)


"""
A -> B

A -> B
B -> C

A -> B
B -> C
C -> D
...
"""
READ_FILENAME, WRITE_FILENAME = 'change.csv', 'after.csv'
BEFORE_STCS, AFTER_STCS = read_csv(READ_FILENAME)

results = []
while AFTER_STCS:
    _, after_stc = BEFORE_STCS.pop(0), AFTER_STCS.pop(0)
    results.append(check(after_stc))

# while AFTER_STCS:
#     before_stc, after_stc = BEFORE_STCS.pop(0), AFTER_STCS.pop(0)
#     result = ''
#     result += check_2(before_stc, after_stc, result)
#     results.append(result)
#
# for r in results:
#     print(r)

write_csv(WRITE_FILENAME, results)
