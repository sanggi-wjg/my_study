import csv
import sys
from typing import Generator, Iterator


def read_csv_generator(filename: str) -> str:
    with open(filename, 'r') as file:
        for row in csv.reader(file):
            yield row[0]


def read_csv_list(filename: str) -> list:
    with open(filename, 'r') as file:
        bank_names = [row[0] for row in csv.reader(file)]
    return bank_names


generator = read_csv_generator("banklist.csv")
iterator = read_csv_list("banklist.csv")
print(sys.getsizeof(generator))
print(sys.getsizeof(iterator))


def loop_generator(data: Generator):
    for n, d in enumerate(data):
        d += f"{n}"


def loop_iterator(data: Iterator):
    for n, d in enumerate(data):
        d += f"{n}"


loop_generator(generator)
loop_iterator(iterator)
