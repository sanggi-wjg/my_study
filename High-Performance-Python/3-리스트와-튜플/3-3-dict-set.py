phonebook_list = [
    ("홍길동", "010-1111-1111"),
    ("김철수", "010-1111-1234"),
    ("국영수", "010-1234-1234"),
]


def find_phonebook_list(phonebook, needle):
    for name, number in phonebook:
        if name == needle:
            return number
    return ''


phonebook_dict = {
    "홍길동": "010-1111-1111",
    "김철수": "010-1111-1234",
    "국영수": "010-1234-1234",
}

# print(find_phonebook_list(phonebook_list, '국영수'))
# print(phonebook_dict['국영수'])
