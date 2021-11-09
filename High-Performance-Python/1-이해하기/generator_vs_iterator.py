import csv
import sys
from typing import Generator, Iterator, Union


def read_csv_generator(filename: str) -> list:
    file = open(filename, 'r')
    try:
        for row in csv.reader(file):
            yield row[0]
    finally:
        file.close()


def read_csv_list(filename: str) -> list:
    file = open(filename, 'r')
    bank_names = []
    try:
        for row in csv.reader(file):
            bank_names.append(row[0])
    finally:
        file.close()

    return bank_names


def loop_generator(data: Iterator):
    for n, d in enumerate(data):
        d += f"{n}"


def loop_iterator(data: Generator):
    for n, d in enumerate(data):
        d += f"{n}"


gc = read_csv_generator("banklist.csv")
lc = read_csv_list("banklist.csv")
print(sys.getsizeof(gc))
print(sys.getsizeof(lc))

loop_generator(gc)
loop_iterator(lc)
