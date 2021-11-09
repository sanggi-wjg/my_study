import csv


def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False


def search_slow(haystack, needle):
    is_exist = False
    for item in haystack:
        if item == needle:
            is_exist = True
    return is_exist


def search_unknown_1(haystack, needle):
    print(type((item == needle for item in haystack)))
    return any((item == needle for item in haystack))


def search_unknown_2(haystack, needle):
    print(type([item == needle for item in haystack]))
    return any([item == needle for item in haystack])


def get_dataset(filename: str) -> list:
    file = open(filename, 'r')
    bank_names = []
    try:
        for row in csv.reader(file):
            bank_names.append(row[0])
    finally:
        file.close()

    return bank_names


haystack = get_dataset('banklist.csv')
needle = 'Hana Bank'

search_fast(haystack, needle)
search_slow(haystack, needle)
search_unknown_1(haystack, needle)
search_unknown_2(haystack, needle)
