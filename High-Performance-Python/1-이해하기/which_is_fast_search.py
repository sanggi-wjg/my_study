import csv


def get_dataset(filename: str) -> list:
    file = open(filename, 'r')
    bank_names = []
    try:
        for row in csv.reader(file):
            bank_names.append(row[0])
    finally:
        file.close()

    return bank_names


def search_1(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False


def search_2(haystack, needle):
    is_exist = False
    for item in haystack:
        if item == needle:
            is_exist = True
    return is_exist


def search_3(haystack, needle):
    # print(type((item == needle for item in haystack)))
    return any((item == needle for item in haystack))


def search_4(haystack, needle):
    # print(type([item == needle for item in haystack]))
    return any([item == needle for item in haystack])


haystack = get_dataset('banklist.csv')
needle = 'Hana Bank'

search_1(haystack, needle)
search_2(haystack, needle)
search_3(haystack, needle)
search_4(haystack, needle)
