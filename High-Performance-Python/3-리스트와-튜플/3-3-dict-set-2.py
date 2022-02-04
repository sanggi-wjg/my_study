phonebook_list = [
    ("홍길동", "010-1111-1111"),
    ("김철수", "010-1111-1234"),
    ("국영수", "010-1234-1234"),
]


def unique_names_list(phonebook):
    unique_names = []
    for name, number in phonebook:
        if name[0] not in unique_names:
            unique_names.append(name[0])
    return unique_names


def unique_names_set(phonebook):
    unique_names = set()
    for name, number in phonebook:
        unique_names.add(name[0])
    return unique_names


print(unique_names_list(phonebook_list))
print(unique_names_set(phonebook_list))
