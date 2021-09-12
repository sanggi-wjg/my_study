def check_password(username: str, password: str) -> bool:
    try:
        user = User.object.get(username = username)

        encrypt = User.object.get_encrypt_password(username = username)
        if password == decrypt_password(encrypt):
            session_initialize()
            return True

    except User.DoseNotExist:
        raise UserDoesNotExist("user is not exist")

    return False


def set_value(key: str, value: str) -> bool:
    my_dict = dict()

    if key not in my_dict.keys():
        my_dict.setdefault(key, value)
        return True
    else:
        return False


def is_exist_key(key):
    my_dict = { 'First': 'A' }
    return key in my_dict.keys()



a = is_exist_key('First')
print(a)

b = is_exist_key('Second')
print(b)
