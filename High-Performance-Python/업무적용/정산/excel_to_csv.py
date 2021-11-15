import csv

import pandas as pd

filename = 'YTO-2021-10-SHA.xlsx'
csv_name = 'YTO-2021-10-SHA.csv'

read_file = pd.read_excel(filename, sheet_name = 1)
read_file.to_csv(csv_name, index = None, header = True)


def read_csv_generator(filename: str) -> str:
    file = open(filename, 'r')
    try:
        for row in csv.reader(file):
            yield row
    finally:
        file.close()


rows = read_csv_generator(csv_name)
